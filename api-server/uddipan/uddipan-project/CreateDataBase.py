import mysql.connector
from config import *


def create():
    mydb = mysql.connector.connect(
        host=config['MYSQL_HOST'],
        user=config['MYSQL_USER'],
        password=config['MYSQL_PASSWORD']
    )

    mycursor = mydb.cursor()
    try:
        mycursor.execute(f"CREATE DATABASE uddipan;")
    except mysql.connector.errors.DatabaseError:
        pass

    mydb.commit()

    mydb = mysql.connector.connect(
        host=config['MYSQL_HOST'],
        user=config['MYSQL_USER'],
        password=config['MYSQL_PASSWORD'],
        database=config['MYSQL_DB']
    )
    mycursor = mydb.cursor()

    with open("sql/ztweet.sql", 'r', encoding="utf-8") as f:
        sqls = f.read().split(";")
        print(len(sqls))
        # mycursor.execute(sqls)
        # mydb.commit()
        for sql in sqls:
            try:
                mycursor.execute(sql)
                mydb.commit()
            except Exception as e:
                pass
