from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import openpyxl
import datetime
import json
import time
import os


finalData_18 = []
productLinks_18 = []
uniqueLnks_18 = []

FinalProductNameList = ['Brancott Estate', 'Matsui Sakura', 'Monte Alban', 'Martell', 'Label', 'Tarantula Azul', 'Tarantula', 'Glenfarclas 21YO', 'Kahlua', 'Don Julio', 'Wyborowa', 'Talisker', 'Saratoga Dark', 'Patron Silver', 'Beefeater 24', 'Veuve Clicquot', 'Veuve', 'Dalwhinnie', 'Glenmorangie Signet', 'Smirnoff Black', 'Courvoisier Premier', 'Wyndham Bin', 'Ketel', "Mackinlay's Shackleton", 'Napkin', 'Fugue De', 'Highland Mist', 'Black &', 'Captain', 'Asahi Super', 'Talisker 10YO', 'Alexander', 'Belvedere', 'Glenrothes', 'Malesan', 'Rail', 'Mortlach 12YO', 'Brancott', 'Moet &', 'Krug Vintage', 'Ron Zacapa', 'Jinro Flavour', 'Sauza Extra', 'Naked', 'Glenmorangie 18YO', 'Courvoisier VSOP', 'Chateau Fonreaud', 'Bowmore', 'St Hugo', 'Royal Salute', 'Demo', "Pimm's Aperitif", 'Absolut Extrakt', 'Glenmorangie Nectar', 'Captain Morgan', 'Absolut Mandrin', 'Kahlua Coffee', 'Wyndham', "Ballantine's 17YO", 'Bottega', 'Diesel 190', 'Nikka Super', 'Fugue', 'Zhuoneng', "Pimm's", 'Bottega Fragolino', "Maker's", 'Monkey', 'Bowmore 12YO', 'Cafe', 'Baileys', 'Nikka From', 'Condiments', 'Patron Reposado', 'Casamigos Anejo', 'The Glenlivet', "Gordon's", 'Rain Organics', 'Royal', 'Ruinart Blanc', 'Hakushu', 'Kronenbourg', 'Martini', 'Malesan Blanc', 'Bowmore 18YO', 'Ice', 'Cocktail Shaker', 'Courvoisier XO', 'Whisky', 'Casamigos Blanco', 'Singleton Dufftown', 'Cup Shot', 'Matsui San-In', 'Cape Mentelle', 'Cragganmore', 'Hennessy Richard', 'Alexander Society', "Chateau D'Armailhac", 'Auchentoshan', '99 Schnapps', 'Sauza', 'Graffigna', 'Mumm', 'Chateau Lafon', 'Jose', 'Wuliangye 52%', 'J&B', 'Montezuma Silver', 'Hennessy Prive', 'Maison Louis', 'Ardmore', 'Smirnoff', 'Glenmorangie 10YO', 'Hine XO', 'Cocktails', 'Montezuma', 'Matsui', 'Ciroc', 'Nikka Taketsuru', 'Napkin Holder', 'Krug Grande', "Hakushu Distiller's", 'Archers', 'Chandon', 'Courvoisier', 'Dalwhinnie 15YO', 'Glenfarclas 15YO', 'Moet', 'Pinnacle', 'Martell XO', 'Olmeca Reposado', 'Malibu', 'Demo Bundle', 'Kronenbourg 1664', 'Wuliangye Mellow', 'Johnnie Walker', 'Mortlach', 'Matsui Kurayoshi', 'Matsui Umeshu', "Maker's Mark", 'Copper', "Teacher's", 'Highland', 'Glen', 'Chandon Brut', 'Terrazas', 'Bottega Gold', "Gordon's Pink", 'Absolut Kurant', 'John Jameson', 'Glenfarclas 17YO', 'Absolut Peach', 'Matsui The', 'John', 'Patron Roca', 'Mortlach 16YO', 'Ruinart Rose', 'Tanqueray', 'Golden Glass', 'Copper Dog', 'Ketel One', 'Aberlour 12YO', 'Hennessy VSOP', 'Chivas', 'di', 'Chateau Latour', 'Maison', 'Martell Noblige', 'Glenfarclas 40YO', 'Hibiki 17YO', "Ballantine's 30YO", 'Lagavulin 16YO', 'Glenkinchie', 'Glenmorangie 14YO', 'Jinro Chamisul', 'Patron Anejo', 'Royal Lochnagar', 'Mumm Cordon', 'Bowmore 25YO', 'Caol ILA', 'Dame De', 'Asahi', 'Corona', 'Yamazaki', 'Condiments Long', 'Clynelish 14YO', 'Jura', "Ballantine's", 'Rail Square', 'Wuliangye', 'The Dalmore', 'Terrazas Altos', 'Havana', 'Jinro Strawberry', 'Bottega Soave', 'Chivas Regal', 'Ruinart', 'Paulaner Weissbier', 'Chateau', 'Ardbeg', 'Casamigos Joven', 'Carlsberg Danish', 'Cocktails by', "Gilbey's", 'Chateau Chauvin', 'Patron', 'Ardbeg 10YO', 'Patron XO', 'Saratoga', 'Campo', 'Crystal', 'Perrier', 'Smirnoff Red', 'Don', 'Paulaner', 'Aberlour', 'Casamigos Reposado', 'Chateau Pichon', 'Malesan Medoc', 'Rocks Glass', 'Casamigos', 'Jinro', 'Bottega Poeti', "Jacob's Creek", 'Cardhu', 'Dame', 'Monkey 47', 'Glenfarclas', 'Jura 18YO', 'Altos Blanco', 'Bottega 0', 'Wine', "Fleischmann's", 'Jinro Plum', 'Somersby Cider', 'Hine', 'Paulaner Munich', 'Absolut Elyx', 'El Recuerdo', 'Talisker 18YO', 'Ron', 'Black', 'Glenfarclas 30YO', 'Matsui Mizunara', 'Ardbeg Corryvreckan', 'Bowmore 12', 'Olmeca', 'Hennessy XO', 'Patron Citronge', 'Rain', 'Graffigna Pinot', 'Bacardi Superior', 'Bulleit', 'McCormick Orange', 'Balvenie', 'Dom Perignon', 'Passport', 'Cantenac Brown', 'Whisky Glass', 'Somersby', 'Krug', 'Glenfarclas 25YO', 'Patron Shot', '99', 'Cocktail', 'Cape', 'Alter', 'Terrazas Reserva', 'Ruinart R', 'Malesan Rouge', 'Royal Dragon', 'Bottega Stardust', 'Cutty Sark', 'Havana Club', 'Martell Chanteloup', 'McCormick Raspberry', 'Mumm Rose', 'McCormick Vanilla', 'Tanqueray Sevilla', 'Tanqueray Rangpur', 'J&B Rare', 'Tanqueray Ten', 'Cafe De', 'Aberlour 16YO', 'Hennessy', 'Jagermeister', 'Chateau Pedesclaux', 'Glenmorangie', 'Golden', 'Cutty', 'Bottega Rose', 'St', 'Carlsberg', 'Altos', 'Tequila', 'Rail Rectangular', 'The', 'Cragganmore 12YO', 'Campo Viejo', 'Belvedere Pink', 'Beefeater', 'Pernod', 'Paulaner Oktoberfest', 'Chateau Du', 'Nikka Coffey', 'Aberlour 18YO', 'Jack DanielÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢s', 'Label 5', 'Cantenac', 'Jura Seven', 'Black Velvet', 'Martell Cordon', 'Naked Grouse', 'Perrier Jouet', 'Penfolds Grange', "Ballantine's 12YO", 'Altos Reposado', 'McCormick Apple', "Teacher's Origin", 'Jura 12YO', 'Rocks', 'Absolut', 'Absolut Citron', 'Glen Grant', 'Dom', 'Penfolds Bin', 'Bulleit Rye', 'Cup', 'Baileys Cream', "Ballantine's 21YO", 'Glenkinchie 12YO', 'Tequila Rose', 'Monte', 'di Amore', 'Cutting', 'Absolut Original', 'Larios', 'Chateau Coutet', 'Martini Alta', 'Diesel', 'Chandon Rose', "Jacob's", 'Auchentoshan 12YO', 'Hibiki', 'Oban', 'Matsui Tottori', 'Jinro Grapefruit', 'Corona Extra', 'Hennessy Paradis', 'Barton', "Ballantine's Finest", 'Ricard', 'Caol', 'Montezuma Triple', 'Clynelish', 'McCormick', 'Jim Beam', 'Chateau Clos', 'Singleton', 'Crystal Head', 'Cardhu 12YO', "Fleischmann's Vanilla", 'Glenfarclas 12YO', 'Belvedere Pure', 'Glenmorangie 12YO', 'Ultimat', 'Ice Bucket', 'Yamazaki 18YO', 'Alter Ego', 'Mumm Blanc', 'Jose Cuervo', 'Balvenie 40YO', 'Martell NCF', 'Absolut Vanilia', 'Bacardi', 'Cloudy', "Mackinlay's", 'Glenrothes Vintage', "Broker's", 'El', 'Penfolds', 'Hibiki 21YO', 'Jim', 'Lagavulin', 'Martell VSOP', 'Montezuma Gold', 'Malibu Coconut', 'Mortlach 20YO', 'Wine Opener', 'Cutting Board', 'Cloudy Bay', 'Archers Peach', 'Oban 14YO', 'Johnnie', 'Jack', 'Bottega Petalo', 'Nikka', 'Ardbeg Uigeadail']

#------------------------------------------


print("--------------------------------------------")

print("Web Scrapper Started Successfully ...")
ct = datetime.datetime.now()
print("Start Time :-", ct)

print("--------------------------------------------")

#-------------------------------------------------------------------------------------

# Functions for Site 13 - "https://cellarbration.com.sg/" -

def get_links_18():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_18.append(ld1)
    except:
        print("Products not found !")


def get_info_18(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product_header"]/div[2]/h1'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1].replace("ml", "")
        volume = int(volume)/10
    except:
        try:
            volume = productName2.split(" ")
            volume = volume[-1]
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div[2]/div[2]/div[1]/div[2]/span/text()[2]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div[2]/div[2]/div[2]/form/span').text
        price = price.replace("S$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Oaks Cellar",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_18.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Driver Code -

# driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')

CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

driver.get("https://www.oaks.com.sg/")

print(">> ", driver.title)

for productName in FinalProductNameList[0:5]:
    surl = "https://www.oaks.com.sg/?keyword=" + productName + "&page=gallery&from=sugg"
    try:
        driver.get(surl)
        get_links_18()
    except:
        print("No product found for search - ", surl)
a = set(productLinks_18)
a = list(set(a))
seen = set()
result = []
for item in a:
    if item not in seen:
        seen.add(item)
        uniqueLnks_18.append(item)
print(uniqueLnks_18)
print(len(uniqueLnks_18))
for lnk2 in uniqueLnks_18:
    get_info_18(lnk2)
    print("Final Data :- ", finalData_18[-1])
    print("No of Product Info. :- ", len(finalData_18))
    print(finalData_18[-1])
clean_data_18 = [i for n, i in enumerate(finalData_18) if i not in finalData_18[n + 1:]]

driver.close()

#-------------------------------------------------------------------------------------


#........................................................................................

# Data Saving for Website - 1

# Saving the Data to Excel Sheet -

df = pd.DataFrame.from_dict(clean_data_18)
print(df)
df.to_excel('dataWeb_18.xlsx', index=False)


# To Save Data in JSON file -
import json

def save_data(title, data):
  with open(title, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(title):
  with open(title, encoding="utf-8") as f:
    return json.load(f)


save_data("dataWeb_18.json", clean_data_18)

#........................................................................................


print("--------------------------------------------")

ct1 = datetime.datetime.now()
print("Start Time :-", ct)
print("End Time :-", ct1)

print("--------------------------------------------")

