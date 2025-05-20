def scrape_temuproduct_links():
    url = "https://temu.to/k/e6xiugmdprq"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/goods.html" in href and href.startswith("http"):
            if href not in links:
                links.append(href)

    print("נמצאו קישורים:", links)
    return links
