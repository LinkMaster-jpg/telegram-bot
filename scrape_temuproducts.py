from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_temuproduct_links():
    url = "https://temu.to/k/e6xiugmdprq"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Give time for JavaScript to load

    links = set()
    elements = driver.find_elements(By.TAG_NAME, "a")
    for el in elements:
        href = el.get_attribute("href")
        if href and "/goods.html" in href and href.startswith("http"):
            links.add(href)

    driver.quit()
    return list(links)