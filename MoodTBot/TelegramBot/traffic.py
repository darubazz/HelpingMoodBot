import requests
from bs4 import BeautifulSoup

URL = "https://yandex.ru/maps/67/tomsk/?l=trf%2Ctrfe&ll=84.988423%2C56.533638&z=10.89"
URL1 = "https://yandex.ru/"
HEADERS = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    'accept': "*/*"}


def get_html(url, params=None):
    html = requests.get(url, headers=HEADERS, params=params)
    return html


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    message = soup.find('div', class_='traffic-panel-view__dropdown-title')
    message.get_text()

    #message = soup.find('div', class_='traffic__rate - text')
    #message.get_text()
    #traffic__rate - text
    #home-link home-link_black_yes
    #message = soup.find('div', class_='home-link home-link_black_yes')
    #message.get_text()
    return message


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('Error')
