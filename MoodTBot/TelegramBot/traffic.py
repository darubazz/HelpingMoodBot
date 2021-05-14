import requests
from bs4 import BeautifulSoup

URL = "https://yandex.ru/"
HEADERS = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    'accept': "*/*"}


def get_html(url, params=None):
    html = requests.get(url, headers=HEADERS, params=params)
    return html


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='film-title')
    traffic = []
    for item in items:
        traffic.append(
            {
                'title': item.find('a').get_text(strip=True),
                'rating': parse_rating(item.find('a').get_text(strip=True))
            }
        )
    return films


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('Error')
