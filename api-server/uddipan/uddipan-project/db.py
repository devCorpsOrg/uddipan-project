# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# from datetime import datetime
# from datetime import date
# from tools import *
# from loguru import logger
# from log import *
# import mysql.connector
# from config import *

# import traceback

# def search_adv(data, productNameList, vol):
#     vol = '70'
#     print(type(vol))
#     for dt in data[0]:
#         priority = 0
#         for pnw in productNameList:
#             if str(pnw.lower()) in str(dt["Product Name"].lower()):
#                 priority = priority + 1
#             if str(vol.replace("ml", "")) in str(dt["Volume"].lower()):
#                 priority = priority + 1
#             else:
#                 continue
#             prt = {"priority" : priority}
#             dt.update(prt)
#     data = sorted(data[0], key=lambda x: x['priority'], reverse=True)

#     if len(data) > 20:
#         data = data[0:20]

#     for dt in data:
#         dt.pop("priority")
    
#     return data

# class db:
#     mysql = None

#     def __init__(self):
#         self.mydb = mysql.connector.connect(
#             host=config['MYSQL_HOST'],
#             user=config['MYSQL_USER'],
#             password=config['MYSQL_PASSWORD'],
#             database=config['MYSQL_DB']
#         )
#         logger.info(f"Datebase Class Created With {str(mysql)}")

#     def getCursor(self):
#         self.mydb.reconnect()
#         return self.mydb.cursor()


#     def select(self, table, search=False, query=None):
#         self.mydb.reconnect()
#         cursor = self.mydb.cursor(buffered=True,dictionary=True)
#         print (query)
#         if query is None:
#             query = {}
#         if search:
#             if query['flag'] :
#                 productName = query['value']
#                 try:
#                     vol = query['value2']
#                 except:
#                     vol = '70'
#                 productName = productName.replace("'", "")
#                 productNameList = productName.split(" ")
#                 data = []
#                 for productName in productNameList:

#                     query = f"SELECT * FROM `{table}` WHERE `{query['query']}` LIKE '%{productName}%' OR '{productName}%' OR '%{productName}'"

#                     cursor.execute(query)
#                     info = cursor.fetchall()
#                     data.append(info)
#                     data = [i for n, i in enumerate(data) if i not in data[n + 1:]]

#                     data = search_adv(data, productNameList, vol)
                    
#                     return data

#             else :
#                 query = f"SELECT * FROM `{table}`"
#             cursor.execute(query)
#             try:
#                 self.mydb.commit()
#             except Exception as e:
#                 logger.error(f"error 55 : {e}")
#                 return []
#             return cursor.fetchall()
#         else:
#             query = f"SELECT * FROM `{table}` WHERE 1"
#             cursor.execute(query)
#             try:
#                 self.mydb.commit()
#             except Exception as e:
#                 logger.error(f"error 64 : {e}")
#                 return []
#             return cursor.fetchall()
#         return None





# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# from datetime import datetime
# from datetime import date
# from tools import *
# from loguru import logger
# from log import *
# import mysql.connector
# from config import *

# import traceback

# def search_adv(data, productNameList, vol):
#     newData = []
#     for dt in data[0]:
#         priority = 0
#         for pnw in productNameList:
#             cVol = dt["Volume"].lower().replace('ml', '').replace('l', '').replace('cl', '')
#             try:
#                 try:
#                     cVol = float(cVol) * 100
#                 except:
#                     cVol = float(cVol.split()[0])*100
#             except:
#                 cVol = 0

#             if str(vol.lower().replace('ml', '').replace('l', '').replace('cl', '')) in str(cVol):
#                 priority = priority + 5
            
#             if str(pnw.lower()) in str(dt["Product Name"].lower()):
#                 priority = priority + 1
            
#             prt = {"priority" : priority}
#             dt.update(prt)
        
#     data1 = sorted(data[0], key=lambda x: x['priority'], reverse=True)
#     data = []
#     for dt2 in data1:
#         if dt2["Volume"] == '' or dt2["Price"] == '':
#             continue
#         else:
#             data.append(dt2)

#     if len(data) > 20:
#         data = data[0:20]

#     try:
#         for dt in data:
#             dt.pop("priority")
#     except:
#         pass
    
#     return data

# class db:
#     mysql = None

#     def __init__(self):
#         self.mydb = mysql.connector.connect(
#             host=config['MYSQL_HOST'],
#             user=config['MYSQL_USER'],
#             password=config['MYSQL_PASSWORD'],
#             database=config['MYSQL_DB']
#         )
#         logger.info(f"Datebase Class Created With {str(mysql)}")

#     def getCursor(self):
#         self.mydb.reconnect()
#         return self.mydb.cursor()


#     def select(self, table, search=False, query=None):
#         self.mydb.reconnect()
#         cursor = self.mydb.cursor(buffered=True,dictionary=True)
#         print (query)
#         if query is None:
#             query = {}
#         if search:
#             if query['flag'] :
#                 productName = query['value']
#                 vol = query['value2']
#                 # print(vol)
#                 productName = productName.replace("'", "")
#                 productNameList = productName.split(" ")
#                 data = []
#                 for productName in productNameList:

#                     query = f"SELECT * FROM `{table}` WHERE `{query['query']}` LIKE '%{productName}%' OR '{productName}%' OR '%{productName}'"

#                     cursor.execute(query)
#                     info = cursor.fetchall()
#                     data.append(info)
#                     data = [i for n, i in enumerate(data) if i not in data[n + 1:]]

#                     data = search_adv(data, productNameList, vol)
                    
#                     return data

#             else :
#                 query = f"SELECT * FROM `{table}`"
#             cursor.execute(query)
#             try:
#                 self.mydb.commit()
#             except Exception as e:
#                 logger.error(f"error 55 : {e}")
#                 return []
#             return cursor.fetchall()
#         else:
#             query = f"SELECT * FROM `{table}` WHERE 1"
#             cursor.execute(query)
#             try:
#                 self.mydb.commit()
#             except Exception as e:
#                 logger.error(f"error 64 : {e}")
#                 return []
#             return cursor.fetchall()
#         return None


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

def search_adv(data, productNameList, vol):
    newData = []
    for dt in data[0]:
        priority = 0
        for pnw in productNameList:
            cVol = dt["Volume"].lower().replace('ml', '').replace('l', '').replace('cl', '')
            try:
                try:
                    cVol = float(cVol) * 100
                except:
                    cVol = float(cVol.split()[0])*100
            except:
                cVol = 0

            if str(vol.lower().replace('ml', '').replace('l', '').replace('cl', '')) in str(cVol):
                priority = priority + 8
            
            if str(pnw.lower()) in str(dt["Product Name"].lower()):
                priority = priority + 1
            
            prt = {"priority" : priority}
            dt.update(prt)
        
    data1 = sorted(data[0], key=lambda x: x['priority'], reverse=True)
    data = []
    for dt2 in data1:
        if dt2["Volume"] == '' or dt2["Price"] == '' or vol not in dt2["Volume"]:
            continue
        else:
            data.append(dt2)

    if len(data) > 20:
        data = data[0:20]
    try:
        for dt in data:
            dt.pop("priority")
    except:
        pass
    
    return data

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
        self.mydb.reconnect()
        return self.mydb.cursor()


    def select(self, table, search=False, query=None):
        self.mydb.reconnect()
        cursor = self.mydb.cursor(buffered=True,dictionary=True)
        print (query)
        if query is None:
            query = {}
        if search:
            if query['flag'] :
                productName = query['value']
                vol = query['value2']
                # print(vol)
                productName = productName.replace("'", "")
                productNameList = productName.split(" ")
                data = []
                for productName in productNameList:

                    query = f"SELECT * FROM `{table}` WHERE `{query['query']}` LIKE '%{productName}%' OR '{productName}%' OR '%{productName}'"

                    cursor.execute(query)
                    info = cursor.fetchall()
                    data.append(info)
                    data = [i for n, i in enumerate(data) if i not in data[n + 1:]]

                    data = search_adv(data, productNameList, vol)
                    
                    return data

            else :
                query = f"SELECT * FROM `{table}`"
            cursor.execute(query)
            try:
                self.mydb.commit()
            except Exception as e:
                logger.error(f"error 55 : {e}")
                return []
            return cursor.fetchall()
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
