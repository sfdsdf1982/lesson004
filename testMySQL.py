from pprint import pprint
import pymysql.cursors
from pymysql import *

# Делаем коннект к базе данных

def show_data(cur):
    cur.execute('select * from goods')  # запустили запрос на сервере базы данных
    rows = cur.fetchall()  # получили все записи из таблицы
    # pprint(rows)
    for item in rows:
        print(f"Автомобиль {item['title']} стоит {item['price']}")
def update(cur):
    info = input("Введите название авто и новую стоимость для этого авто через дефис\n").split("-")
    title = info[0]
    price = int(info[1])
    str_sql = f"UPDATE goods SET price={price} where title='{title}'"
    cur.execute(str_sql)


connect = connect(host="localhost",
                  user="root",
                  password="root",
                  db="les03",
                  cursorclass=pymysql.cursors.DictCursor #для возможности работать с данными из таблицы в виде словаря
                  )
with connect:
    cur = connect.cursor() #получили объект с помощью которого можно запускать запросы на сервере базы данных
    show_data(cur)
    update(cur)
    connect.commit() #для подтвеждения изменения данных в базе
    print("После обновления")
    show_data(cur)
