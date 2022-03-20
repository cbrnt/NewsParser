import os

from bs4 import BeautifulSoup
from datetime import datetime
from lib.news import News

URL = os.environ['URL']
DB_PATH = os.environ['DB_PATH']

if __name__ == '__main__':
    news = News(URL, DB_PATH)
    html = news.get_page()
    soup = BeautifulSoup(html, 'lxml')
    posts = []

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
                posts.append(new_one)
                count += 1

    result = news.save_posts(posts)
    read_result = news.read_db()

    print('READ', '\n', read_result)
