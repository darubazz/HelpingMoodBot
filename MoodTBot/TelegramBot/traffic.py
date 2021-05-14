import requests
from bs4 import BeautifulSoup

URL = "https://yandex.ru/"
HEADERS = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    'accept': "*/*"}