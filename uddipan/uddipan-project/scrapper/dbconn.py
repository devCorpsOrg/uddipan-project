from sqlalchemy import create_engine
import pandas as pd
import pymysql
import sys, os
import openpyxl
#........................................................................................

# To Store Scraped Data in MYSQL Database (Remote Database) -

#1
engine = create_engine("mysql+pymysql://dev:devAverps3985$$@34.142.195.183/uddipan?charset=utf8mb4")
df = pd.read_json("finalData.json")
df.to_sql("Product_prices", con=engine, if_exists="replace", index=False)
 
#........................................................................................

#engine = create_engine("mysql+pymysql://" + "dev" + ":" + "devAverps3985$$" + "@" + "34.142.195.183" + "/" + "uddipan" + "?" + "charset=utf8mb4")
#conn = engine.connect()
#excel_file = pd.read_excel("finalData.xlsx",engine='openpyxl')
##excel_dataframe = excel_file.parse(sheetname=1)
#excel_file.to_sql("new_products", conn, if_exists="replace", index=False)

#2
#engine = create_engine("mysql+pymysql://dev:devAverps3985$$@34.142.195.183/uddipan?charset=utf8mb4")
#conn = engine.connect()
#excel_file = pd.ExcelFile('finalData.xlsx')
#excel_dataframe = excel_file.parse(sheetname=1)
#excel_dataframe.to_sql("Product_prices", conn, if_exists="replace", index=False)



#from sqlalchemy import create_engine
#import pandas as pd
#import pymysql
##........................................................................................
#
## To Store Scraped Data in MYSQL Database (Remote Database) -
#
#engine = create_engine("mysql://dev:devAverps3985$$@34.142.195.183/uddipan")
#df = pd.read_json("finalData.json","r", encoding="utf8")
#df.to_sql("Product_prices", con=engine, if_exists="replace", index=False)
# 
##........................................................................................