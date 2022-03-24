import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}


def get_price(links):
    for i in links:

        if "amazon" in links[i]:
            print("[₹{price}] Amazon".format(price=amazon(links[i])))

        if "flipkart" in links[i]:
            print("[₹{price}] Flipkart".format(price=flipkart(links[i])))

        if "imagineonline" in links[i]:
            print("[₹{price}] Imagineonline".format(price=imagineonline(links[i])))

        if "reliancedigital" in links[i]:
            print("[₹{price}] Reliancedigital".format(price=reliancedigital(links[i])))


# def apple(url):


def amazon(url):
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    req = soup.find_all('span', "a-offscreen")
    for final in req:
        return final.text.strip()[1:-3]


# def croma(url):


def flipkart(url):
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    req = soup.find_all('div', "_30jeq3 _16Jk6d")
    for final in req:
        return final.text.strip()[1:]


def imagineonline(url):
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    req = soup.find_all('span', attrs={"itemprop": "price"})
    for final in req:
        return final.text.strip()[4:]


def reliancedigital(url):
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    req = soup.find_all('span', "pdp__offerPrice")
    for final in req:
        return final.text.strip()[1:-3]
