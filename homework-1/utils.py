import psycopg2
import csv


def get_customer_data(path="../homework-1/north_data/customers_data.csv"):
    '''Получаем данные из customers_data.csv в виде списка кортежей'''
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            data = [(row['customer_id'], row['company_name'], row['contact_name']) for row in reader]
    except FileNotFoundError:
        print("Файл не найден")
    return data


def get_employees_data(path="../homework-1/north_data/employees_data.csv"):
    '''Получаем данные из employees_data.csv в виде списка кортежей'''
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            data = [(row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes']) for row in
                    reader]
    except FileNotFoundError:
        print("Файл не найден")
    return data


def get_orders_data(path="../homework-1/north_data/orders_data.csv"):
    '''Получаем данные из orders_data.csv в виде списка кортежей'''
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            data = [(row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']) for
                    row in reader]
    except FileNotFoundError:
        print("Файл не найден")
    return data


def sent_data(data: list, table: str):
    ''' Отправляем данные, полученные из csv файла в соответствующую таблицу базы данных'''
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='006711Vf')
    try:
        with conn:
            with conn.cursor() as cur:
                values = "%s, " * len(data[0])
                cur.executemany(f'INSERT INTO {table} VALUES ({values[:-2]})', data)
    except psycopg2.Error:
        print("Ошибка запроса")
    finally:
        conn.close()
