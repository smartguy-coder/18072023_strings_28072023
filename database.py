import sqlite3
import hashlib
from pprint import pprint


def encript_password(value: str) -> str:
    hashed_value = hashlib.md5(value.encode()).hexdigest()
    print(hashed_value)
    return hashed_value


with sqlite3.connect('new_db.sqlite3') as connection:
    cursor = connection.cursor()
    connection.create_function('encode', 1, encript_password)
    cursor.execute("PRAGMA foreign_keys = ON")

    # values = ['phones', 'samsung']
    # query = """
    #     INSERT INTO category(name, description)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)

    # values = ['M12 v2 2023-1-1', 250, 300, 7]
    # query = """
    #     INSERT INTO device(title, whole_price, price, category_id)
    #     VALUES(?, ?, ?, ?)
    # """
    # cursor.execute(query, values)

    # query = """
    #     SELECT device.title, whole_price, price * 1.2, name, category.description
    # FROM device
    #                  LEFT JOIN category
    #     ON device.category_id = category.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())


    # trigger_sql_discount = """
    #     CREATE TRIGGER IF NOT EXISTS discount_description_pr
    #     AFTER UPDATE ON device
    #     WHEN old.price > new.price
    #     BEGIN
    #         UPDATE device
    #         SET description = UPPER('discount') ||  new.price
    #         WHERE id=new.id;
    #     END;
    # """
    # cursor.execute(trigger_sql_discount)

    # trigger_sql_discount = """
    #     CREATE TRIGGER IF NOT EXISTS prem_category
    #     AFTER UPDATE ON device
    #     WHEN new.price > 5000
    #     BEGIN
    #         INSERT INTO category (name, description)
    #         VALUES ('new premium category', 'top' || new.price);
    #     END;
    # """
    # cursor.execute(trigger_sql_discount)

    trigger_sql_some_new_with_condition = """
        CREATE TRIGGER IF NOT EXISTS title_validate
        AFTER UPDATE ON device
        BEGIN
            SELECT
                CASE
                    WHEN length(new.title) > 10 THEN
                        RAISE (ABORT, 'Too long title')
                    END;
        END;
    """
    cursor.execute(trigger_sql_some_new_with_condition)

    query = """
        UPDATE device
        SET
            title = '0123456789'
        WHERE
            id = 10
    """
    cursor.execute(query)


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

    # query = """
    #     CREATE TABLE IF NOT EXISTS category(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name VARCHAR(16) NOT NULL,
    #         description TEXT
    #     );
    #     CREATE TABLE IF NOT EXISTS device(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         title TEXT NOT NULL UNIQUE,
    #         whole_price DECIMAL(10, 2) CHECK (whole_price > 0),
    #         price DECIMAL(10, 2) CHECK (price >= whole_price),
    #         category_id INTEGER,
    #         FOREIGN KEY (category_id) REFERENCES category(id)
    #     )
    # """
    # cursor.executescript(query)


    # CREATE
    # name = 'Max'
    # password = '123456'
    # login = 'qwerty3'
    # values = [name, login, password]
    #
    # query = """
    #     INSERT INTO user(name, login, password)
    #     VALUES (?, ?, encode(?))
    # """
    # cursor.execute(query, values)

    # insert many
    # values = (
    #     ('1', '2234545', '3'),
    #     ('1', '22rtytry34545', '3'),
    #     ('1', '2234fgh545', '3'),
    # )
    #
    # query = """
    #     INSERT INTO user(name, login, password)
    #     VALUES (?, ?, encode(?))
    # """
    # cursor.executemany(query, values)
    #     #####################################

    # READ
    # query = """
    #     SELECT name, address
    #     FROM user
    #     WHERE id >= 3
    # """
    # query = """
    #     SELECT name, address
    #     FROM user
    #     WHERE id > 3 AND address = 'Київ'
    # """
    # query = """
    #     SELECT name, address
    #     FROM user
    #     WHERE id > 3 AND address LIKE '%Київ%'
    # """
    # query = """
    #     SELECT name, address
    #     FROM user
    #     WHERE id BETWEEN 3 and 6
    # """
    # query = """
    #     SELECT name, address
    #     FROM user
    #     WHERE id = 3 OR name LIKE '1%'
    #     ORDER BY id DESC
    #     LIMIT 3
    #     OFFSET 2
    # """
    #
    # result = cursor.execute(query)
    # # print(result.fetchmany(size=3))
    # print(result.fetchall())
    # print(result.fetchone())
    # print(result.__next__())
    # print(result.__next__())
    # print(result.__next__())

    # UPDATE
    # query = """
    #     UPDATE user
    #     SET
    #         address = 'Odesa'
    #     WHERE
    #         id > 4
    # """
    # query = """
    #     UPDATE customers
    #     SET
    #         email = LOWER('mr_' || name || '_' || id || '@gmail.com')
    # """

    # query = """
    #     UPDATE user
    #     SET
    #         password = :Pass
    #     WHERE
    #         id = 3
    # """
    #
    # cursor.execute(query, {'Pass': 'e10adc3949ba59abbe56e057f20f883e'})

    # RENAME TABLE
    # query = """
    #     ALTER TABLE user
    #     RENAME TO customers
    # """
    # cursor.execute(query)

    # # RENAME COLUMN
    # query = """
    #     ALTER TABLE customers
    #     RENAME COLUMN address TO email
    # """
    # cursor.execute(query)

    # ADD COLUMN
    # query = """
    #     ALTER TABLE customers
    #     ADD COLUMN conflict BOOLEAN DEFAULT TRUE
    # """
    # cursor.execute(query)

    # query = """
    #     UPDATE customers
    #     SET
    #         balance = 10
    #     WHERE
    #         balance = 5
    # """
    # cursor.execute(query)

    # print(connection.total_changes)
    # # 1/0
    # query = """
    #     UPDATE customers
    #     SET
    #         balance = 11
    #     WHERE
    #         balance = 10
    # """
    # # cursor.execute(query)
    # DELETE
    # query = """
    #     DELETE FROM customers
    #     WHERE
    #         name LIKE '1%'
    # """

    # cursor.execute(query)

    # sqlite_data = 'SELECT sqlite_version()'
    # cursor.execute(sqlite_data)
    # record = cursor.fetchone()
    # print(record)
    #
    # print(connection.total_changes)

    #     CREATE DUMP
    # with open('dump_db.sql', 'w') as dump:
    #     for sql in connection.iterdump():
    #         dump.write(sql)
    # with open('dump_db.sql', 'r') as dump:
    #     sql = dump.read()
    #     cursor.executescript(sql)


# con2 = sqlite3.connect('new_db.sqlite3')
# try:
#     query = """
#         UPDATE customers
#         SET
#             balance = 15
#         WHERE
#             balance = 10
#     """
#     con2.execute(query)
#
#     print(con2.total_changes)
#     1/0
#     query = """
#         UPDATE customers
#         SET
#             balance = 11
#         WHERE
#             balance = 15
#     """
#     con2.execute(query)
#     con2.commit()
# except:
#     con2.rollback()
#     pass
# finally:
#     con2.close()

