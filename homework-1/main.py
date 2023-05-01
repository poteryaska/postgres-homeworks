"""Скрипт для заполнения данными таблиц в БД Postgres."""
from utils import get_customer_data, get_employees_data, get_orders_data, sent_data
def main():
    customer_data = get_customer_data()
    sent_data(customer_data, 'customers')
    employees_data = get_employees_data()
    sent_data(employees_data, 'employees')
    orders_data = get_orders_data()
    sent_data(orders_data, 'orders')

if __name__ == '__main__':
    main()