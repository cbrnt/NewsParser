import logging
import sqlite3
from sqlite3 import Error

import requests


class News:
    """Keeps new Hacker posts attributes."""

    db_file = 'HackerNews/posts.sqlite3'

    def __init__(self, url):
        self.url = url
        self.db_connect = sqlite3.connect(News.db_file)
        self.session = requests.Session()

    def get_page(self) -> str:
        """Gets HTML page body via requests."""
        request = self.session.get(self.url)
        return request.text

    def save_to_db(self, data: list):
        """Saving posts to database."""
        for item in data:
            query = 'INSERT INTO api_news VALUES (?, ?, ?, ?)'
            values = [
                item['id'],
                item['title'],
                item['url'],
                item['created']
            ]
            cur = self.db_connect.cursor()
            try:
                cur.execute(query, (values,))
            except Error as e:
                logging.error(f'SQL error occurred while writing to DB: {str(e)}')
        return 'updated'

    def read_db(self):
        """Get posts from database."""
        query = 'SELECT id, title, url, created FROM api_news'
        cur = self.db_connect.cursor()
        cur.execute(query)
        return cur.fetchall()
