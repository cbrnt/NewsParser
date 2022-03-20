import logging
import sqlite3
from sqlite3 import Error

import requests


class News:

    def __init__(self, url, db_path):
        self.url = url
        self.db_connect = sqlite3.connect(db_path)
        self.session = requests.Session()

    def get_page(self) -> str:
        """Gets HTML page body via requests."""
        request = self.session.get(self.url)
        return request.text

    def check_record(self, post_id: int) -> bool:
        """Checks record existing in table."""
        cur = self.db_connect.cursor()
        query = """SELECT EXISTS(SELECT 1 FROM api_news WHERE id = :id)
        """
        try:
            with self.db_connect:
                print('SELECT EXIST')
                print(post_id)
                print(cur.execute(query, {'id': post_id}))
                # print('FETCH ', cur.fetchone())
                check = cur.fetchone()
                print(type(check[0]))
                print(check[0])
        except Error as e:
            logging.error(f'SQL error occurred while writing to DB: {str(e)}')
        if check[0] == 1:
            return True
        else:
            return False

    def save_posts(self, data: list):
        """Saves posts to database."""
        cur = self.db_connect.cursor()
        for item in data:
            # checking records existing

            if self.check_record(item['id']):
                query = """UPDATE api_news
                           SET id = :id,
                               title = :title,
                               url = :url,
                               created = :created
                           WHERE id = :id"""
            else:
                query = 'INSERT INTO api_news VALUES (:id, :title, :url, :created)'

            try:
                with self.db_connect:
                    cur.execute(query, {
                        'id': item['id'],
                        'title': item['title'],
                        'url': item['url'],
                        'created': item['created'],
                    })
            except Error as e:
                logging.error(f'SQL error occurred while writing to DB: {str(e)}')
        return 'updated'

    def read_db(self):
        """Get posts from database."""
        query = 'SELECT id, title, url, created FROM api_news'
        cur = self.db_connect.cursor()
        cur.execute(query)
        return cur.fetchall()
