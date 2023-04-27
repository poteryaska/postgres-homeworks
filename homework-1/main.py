"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


# def instantiate_from_csv(cls, data='../src/items.csv'):
#     '''инициализирует экземпляры класса Item из файла src/items.csv'''


with open(data='../north_data/customers_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    all = []
    for row in reader:
        if row['name'] and row['price'] and row['quantity'] is not None:
            all.append(row['name'], row['price'], row['quantity'])#connect to db


with psycopg2.connect(host='localhost', database='north', user='postgres', password='006711Vf') as conn:
    with conn.cursor() as cur:
            # execute query
        cur.execute('INSERT INTO user_account Values (%s, %s)', (6, 'Jek'))

        cur.execute('SELECT * FROM user_account')
        rows = cur.fetchall()
        for row in rows:
            print(row)
            #close cursor and close connection

conn.close()