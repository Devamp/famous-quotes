"""
This structure of the DB can be created with the following SQL:

    CREATE TABLE quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        author TEXT,
        date DATE,
        srcType TEXT,
        src TEXT,
        rating INTEGER
    );

To insert a quote into the database, we can use the following SQL:

    INSERT INTO quotes (quote, author, date, source_type, source, rating)
    VALUES ('Your quote text', 'Author Name', '2022-01-31', 'Source Type', 'Source Title', 5);
"""

import sqlite3
from datetime import datetime
from Model import Model

DB_FILE = "quotes.db"


class model(Model):
    def __init__(self):
        # Establish a connection to the SQLite database and create the 'quotes' table if not exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote TEXT,
                author TEXT,
                date DATE,
                srcType TEXT,
                src TEXT,
                rating INTEGER
            )
        """
        )
        cursor.close()

    def select(self):
        # Retrieve all quotes from the 'quotes' table
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quotes")
        return cursor.fetchall()

    def insert(self, quote, author, date, srcType, src, rating):
        # Insert a new quote into the 'quotes' table with provided values
        params = {
            "quote": quote,
            "author": author,
            "date": date,
            "srcType": srcType,
            "src": src,
            "rating": rating,
        }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO quotes (quote, author, date, srcType, src, rating) VALUES (:quote, :author, :date, :srcType, :src, :rating)",
            params,
        )
        connection.commit()
        cursor.close()
