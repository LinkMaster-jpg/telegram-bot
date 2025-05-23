import requests
from bs4 import BeautifulSoup

def scrape_temuproduct_links():
    url = "https://temu.to/k/e6xiugmdprq"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/goods.html" in href and href.startswith("http"):
            if href not in links:
                links.append(href)
    return links
