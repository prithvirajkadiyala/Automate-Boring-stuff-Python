import bs4, requests

def getProductPrice(productUrl):
    res = requests.get(productUrl, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#landingpage-price > div > div > ul > li.price-current')
    return elems[0].text.strip()



price = getProductPrice('https://www.newegg.com/black-asus-tuf-gaming-vg27wq-90lm05f0-b01eb0-27/p/N82E16824281049?Item=N82E16824281049')
print('The price is ' + price)