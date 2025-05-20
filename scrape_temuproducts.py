from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_temuproducts():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.temu.com/')

    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(10):  # גלול 10 פעמים
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    product_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/product/"]')
    links = []
    for elem in product_elements:
        href = elem.get_attribute('href')
        if href and href not in links:
            links.append(href)

    driver.quit()

    with open('links.txt', 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link + '\n')

if __name__ == "__main__":
    scrape_temuproducts()
