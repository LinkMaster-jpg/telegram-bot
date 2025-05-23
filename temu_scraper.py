import requests
from bs4 import BeautifulSoup

def get_product_links():
    url = "https://temu.to/k/e6xiugmdprq"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/goods.html" in href and href.startswith("http"):
            links.add(href)

    return list(links)
