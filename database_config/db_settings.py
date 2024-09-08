import psycopg2
from psycopg2.extras import DictCursor

from .config import DB_CONFIG


class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()

        if self.conn is not None:
            self.conn.close()

        if self.cursor is not None:
            self.cursor.close()

    def execute(self, query, params=None):
        """execute the query(INSERT, UPDATE, DELETE)"""
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=None):
        """fetch many row from the database"""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        """fetch only one row from the database"""
        self.cursor.execute(query, params)
        return self.cursor.fetchone()


def execute_query(query, params=None, fetch=None):
    try:
        with Database() as db:
            if fetch == "all":
                return db.fetchall(query, params)
            elif fetch == "one":
                return db.fetchone(query, params)
            else:
                db.execute(query, params)
    except Exception as e:
        print(f"Exception occurred while executing: {e}")
