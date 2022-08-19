from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import datetime
from datetime import date
from tools import *
from loguru import logger
from log import *
import mysql.connector
from config import *

import traceback

class db:
    mysql = None

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=config['MYSQL_HOST'],
            user=config['MYSQL_USER'],
            password=config['MYSQL_PASSWORD'],
            database=config['MYSQL_DB']
        )
        logger.info(f"Datebase Class Created With {str(mysql)}")

    def getCursor(self):
        return self.mydb.cursor()


    def select(self, table, search=False, query=None):
        cursor = self.mydb.cursor(buffered=True,dictionary=True)
        print (query)
        if query is None:
            query = {}
        if search:
            productName = query['value']
            productName = productName.replace("'", "")
            productNameList = productName.split(" ")
            data = []
            for productName in productNameList:
                if query['flag'] :
                    query = f"SELECT * FROM `{table}` WHERE `{query['query']}` LIKE '%{productName}%' OR '{productName}%' OR '%{productName}'"
                else :
                    query = f"SELECT * FROM `{table}`"
                cursor.execute(query)
                try:
                    self.mydb.commit()
                except Exception as e:
                    logger.error(f"error 55 : {e}")
                    return []

                info = cursor.fetchall()
                data.append(info)
                clean_data = [i for n, i in enumerate(data) if i not in data[n + 1:]]
                return clean_data
        else:
            query = f"SELECT * FROM `{table}` WHERE 1"
            cursor.execute(query)
            try:
                self.mydb.commit()
            except Exception as e:
                logger.error(f"error 64 : {e}")
                return []
            return cursor.fetchall()
        return None