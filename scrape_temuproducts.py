import requests
from bs4 import BeautifulSoup

def scrape_temuproduct_links():
    url = "https://www.temu.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/goods.html?" in href:
            full_link = href if href.startswith("http") else f"https://www.temu.com{href}"
            if full_link not in links:
                links.append(full_link)
    return links
