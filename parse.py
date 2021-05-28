import requests
from bs4 import BeautifulSoup

# text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

URL = 'https://www.gismeteo.ru/weather-surgut-3994/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept': '*/*'
}
s = BeautifulSoup()


def get_html(url, params=None):
    res = requests.get(url, headers=HEADERS, params=params)
    return res


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("h1", class_='firstHeading')
    print(items)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")


parse()
