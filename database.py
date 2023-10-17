import sqlite3


with sqlite3.connect('new_db.sqlite3') as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS user(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name TEXT NOT NULL,
    #         login TEXT NOT NULL CHECK (length(login) > 3) UNIQUE,
    #         password TEXT NOT NULL,
    #         address TEXT
    #     )
    # """
    # cursor.execute(query)

    query = """
        CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(16) NOT NULL,
            description TEXT
        );
        CREATE TABLE IF NOT EXISTS device(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title TEXT NOT NULL UNIQUE,
            whole_price DECIMAL(10, 2) CHECK (whole_price > 0),
            price DECIMAL(10, 2) CHECK (price >= whole_price),
            category_id INTEGER,
            FOREING KEY (category_id) REFERENCES category(id)
        )
    """
    cursor.execute(query)
