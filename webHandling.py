import requests
from bs4 import BeautifulSoup

"""This method is to get html from target url and extract target data"""""


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except requests.RequestException as e:
        print(f"unable get target url: {e}")
        return None


"""This method is to parse html and handling target data"""


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 提取所有新闻标题
    news_titles = soup.find_all(class_='reference internal')

    # 打印新闻标题
    for title in news_titles:
        print(title.text.strip())
