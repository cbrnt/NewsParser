from bs4 import BeautifulSoup
from datetime import datetime
import requests

import lxml
import django
import djangorestframework



def get_page():
    request = requests.get('https://news.ycombinator.com/')
    return request.text


if __name__ == '__main__':
    html = get_page()
    soup = BeautifulSoup(html, 'lxml')
    news = []

    refs = soup.find_all('a', href=True)
    # td = soup.find_all('td', class_='title')
    count = 1
    for ref in refs:
        if ref.attrs.get('class'):
            if 'titlelink' in ref.attrs.get('class'):
                # print(ref.text, '\n', ref.attrs.get('href'))
                new_one = {
                    "id": count,
                    "title": ref.text,
                    "url": ref.attrs.get('href'),
                    'created': datetime.now()
                }
                news.append(new_one)
                count += 1

    print(news)
