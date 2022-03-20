import logging
import sqlite3
from sqlite3 import Error


class Posts:
    """Read and write posts via database."""

    def __init__(self, db_path):
        self.db_connect = sqlite3.connect(db_path)

    def check(self, post_id: int) -> bool:
        """Checks record existing in table."""
        cur = self.db_connect.cursor()
        query = """SELECT EXISTS(SELECT 1 FROM api_news WHERE id = :id)
        """
        try:
            with self.db_connect:
                cur.execute(query, {'id': post_id})
                check = cur.fetchone()
        except Error as e:
            logging.error(f'SQL error occurred while writing to DB: {str(e)}')
        if check[0] == 1:
            return True
        else:
            return False

    def update(self, item: dict):
        """Updates posts in database."""
        cur = self.db_connect.cursor()
        query = """UPDATE api_news
                   SET id = :id,
                       title = :title,
                       url = :url,
                       created = :created
                   WHERE id = :id"""
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
            return False
        return True

    def insert(self, item):
        cur = self.db_connect.cursor()
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
            return False
        return True

    def select(self):
        """Get posts from database."""
        query = 'SELECT id, title, url, created FROM api_news'
        cur = self.db_connect.cursor()
        cur.execute(query)
        return cur.fetchall()
