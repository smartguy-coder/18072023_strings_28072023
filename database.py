import sqlite3


with sqlite3.connect('new_db.sqlite3') as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE user(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            login TEXT NOT NULL CHECK (length(login) > 3) UNIQUE,
            password TEXT NOT NULL,
            address TEXT
        )
    """


