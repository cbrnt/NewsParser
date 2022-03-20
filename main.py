import os
import time

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lib.posts import Posts

URL = os.environ['URL']
DB_PATH = os.environ['DB_PATH']


def get_page(url: str, session_: requests) -> str:
    """Gets HTML page body via requests."""
    request = session_.get(url)
    return request.text


if __name__ == '__main__':
    session = requests.Session()
    news = Posts(DB_PATH)
    while True:
        html = get_page(URL, session)
        soup = BeautifulSoup(html, 'lxml')
        posts = []
        refs = soup.find_all('a', href=True)
        count = 1
        for ref in refs:
            if ref.attrs.get('class'):
                if 'titlelink' in ref.attrs.get('class'):
                    new_one = {
                        "id": count,
                        "title": ref.text,
                        "url": ref.attrs.get('href'),
                        'created': datetime.now()
                    }
                    posts.append(new_one)
                    count += 1

        for post in posts:
            if news.check(post['id']):
                news.update(post)
            else:
                news.insert(post)
        time.sleep(10)

