import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def create_products(conn):
    try:
        create_product(conn, ("Алькони", 78.2, 7))
        create_product(conn, ("Сосиски", 250.4, 26))
        create_product(conn, ("Колбаса", 300.5, 16))
        create_product(conn, ("Хлеб", 30.5, 50))
        create_product(conn, ("Сыр", 125.5, 25))
        create_product(conn, ("молоко", 15.5, 30))
        create_product(conn, ("Кефир", 50.5, 15))
        create_product(conn, ("Жвачка", 5.5, 10))
        create_product(conn, ("Чипсы", 220.5, 5))
        create_product(conn, ("Фанта", 85.5, 12))
        create_product(conn, ("Сырок", 85.5, 12))
        create_product(conn, ("Pepsi", 110.5, 12))
        create_product(conn, ("Сникерс", 30.6, 20))
        create_product(conn, ("Альбени", 27.3, 20))
        create_product(conn, ("Йогурт", 25.5, 10))
    except Error:
        print(Error)


def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        product_list = cursor.fetchall()
        for product in product_list:
            print(product)
    except Error:
        print(Error)


def select_all_products_by_quantity_and_price(conn):
    try:
        sql = '''SELECT * FROM products WHERE quantity > 5 and price < 100.00'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        print(rows)

    except Error:
        print(Error)

def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


connection = create_connection("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print("Connected Success!")
    # select_all_products(connection)
    # delete_products(connection, 14)
    # create_products(connection)
    # update_product_quantity(connection, (8, 7))
    # update_product_price(connection, (45, 1))
    select_all_products(connection)