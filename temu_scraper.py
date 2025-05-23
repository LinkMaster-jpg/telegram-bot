import requests
from bs4 import BeautifulSoup

def scrape_temuproduct_links():
    url = "https://temu.to/k/e6xiugmdprq"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/goods.html" in href and href.startswith("http"):
            links.add(href)

    return list(links)
