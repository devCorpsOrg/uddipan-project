from sqlalchemy import create_engine
import pandas as pd
import pymysql
#........................................................................................

# To Store Scraped Data in MYSQL Database (Remote Database) -
try:
  engine = create_engine("mysql+pymysql://adam:password@localhost/uddipan")
  df = pd.read_json("finalData.json")
  df.to_sql("Product_prices", con=engine, if_exists="replace", index=False)
  print("Data updated in Database...")
except:
  print(">> Cannot Connect to Database")
 
#........................................................................................