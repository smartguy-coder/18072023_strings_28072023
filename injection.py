import sqlite3
import hashlib


def encript_password(value: str) -> str:
    hashed_value = hashlib.md5(value.encode()).hexdigest()
    print(hashed_value)
    return hashed_value


with sqlite3.connect('new_db.sqlite3') as connection:
    cursor = connection.cursor()
    connection.create_function('encode', 1, encript_password)
    # name = 'Max'
    # password = '123456'
    # login = 'qwerty3'
    # values = [name, login, password]
    login = input('Enter login')
    # fake_login', 'fake_pass'); INSERT INTO customers(name, login, password) VALUES ('M', 'DDDDD', '65656');--
    # fake_login2', 'fake_pass'); ALTER TABLE customers RENAME TO users;--

    query = f"""
        INSERT INTO customers(name, login, password)
        VALUES ('Axe', '{login}', 'ljkehgjkfdhg')
    """
    cursor.executescript(query)


