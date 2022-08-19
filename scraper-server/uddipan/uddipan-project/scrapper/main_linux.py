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

# ------------------------------------------

# Global -

finalData_1 = []
productLinks_1 = []
uniqueLnks_1 = []

finalData_2 = []
productLinks_2 = []
uniqueLnks_2 = []

finalData_3 = []
productLinks_3 = []
uniqueLnks_3 = []

finalData_4 = []
productLinks_4 = []
uniqueLnks_4 = []

finalData_5 = []
productLinks_5 = []
uniqueLnks_5 = []

finalData_6 = []
productLinks_6 = []
uniqueLnks_6 = []

finalData_7 = []
productLinks_7 = []
uniqueLnks_7 = []

finalData_8 = []
productLinks_8 = []
uniqueLnks_8 = []

finalData_9 = []
productLinks_9 = []
uniqueLnks_9 = []

finalData_10 = []
productLinks_10 = []
uniqueLnks_10 = []

finalData_11 = []
productLinks_11 = []
uniqueLnks_11 = []

finalData_12 = []
productLinks_12 = []
uniqueLnks_12 = []

finalData_13 = []
productLinks_13 = []
uniqueLnks_13 = []

finalData_14 = []
productLinks_14 = []
uniqueLnks_14 = []

finalData_15 = []
productLinks_15 = []
uniqueLnks_15 = []

finalData_16 = []
productLinks_16 = []
uniqueLnks_16 = []

finalData_17 = []
productLinks_17 = []
uniqueLnks_17 = []

finalData_18 = []
productLinks_18 = []
uniqueLnks_18 = []

finalData_19 = []
productLinks_19 = []
uniqueLnks_19 = []

FinalProductNameList = ['Brancott Estate', 'Matsui Sakura', 'Monte Alban', 'Martell', 'Label', 'Tarantula Azul', 'Tarantula', 'Glenfarclas 21YO', 'Kahlua', 'Don Julio', 'Wyborowa', 'Talisker', 'Saratoga Dark', 'Patron Silver', 'Beefeater 24', 'Veuve Clicquot', 'Veuve', 'Dalwhinnie', 'Glenmorangie Signet', 'Smirnoff Black', 'Courvoisier Premier', 'Wyndham Bin', 'Ketel', "Mackinlay's Shackleton", 'Napkin', 'Fugue De', 'Highland Mist', 'Black &', 'Captain', 'Asahi Super', 'Talisker 10YO', 'Alexander', 'Belvedere', 'Glenrothes', 'Malesan', 'Rail', 'Mortlach 12YO', 'Brancott', 'Moet &', 'Krug Vintage', 'Ron Zacapa', 'Jinro Flavour', 'Sauza Extra', 'Naked', 'Glenmorangie 18YO', 'Courvoisier VSOP', 'Chateau Fonreaud', 'Bowmore', 'St Hugo', 'Royal Salute', 'Demo', "Pimm's Aperitif", 'Absolut Extrakt', 'Glenmorangie Nectar', 'Captain Morgan', 'Absolut Mandrin', 'Kahlua Coffee', 'Wyndham', "Ballantine's 17YO", 'Bottega', 'Diesel 190', 'Nikka Super', 'Fugue', 'Zhuoneng', "Pimm's", 'Bottega Fragolino', "Maker's", 'Monkey', 'Bowmore 12YO', 'Cafe', 'Baileys', 'Nikka From', 'Condiments', 'Patron Reposado', 'Casamigos Anejo', 'The Glenlivet', "Gordon's", 'Rain Organics', 'Royal', 'Ruinart Blanc', 'Hakushu', 'Kronenbourg', 'Martini', 'Malesan Blanc', 'Bowmore 18YO', 'Ice', 'Cocktail Shaker', 'Courvoisier XO', 'Whisky', 'Casamigos Blanco', 'Singleton Dufftown', 'Cup Shot', 'Matsui San-In', 'Cape Mentelle', 'Cragganmore', 'Hennessy Richard', 'Alexander Society', "Chateau D'Armailhac", 'Auchentoshan', '99 Schnapps', 'Sauza', 'Graffigna', 'Mumm', 'Chateau Lafon', 'Jose', 'Wuliangye 52%', 'J&B', 'Montezuma Silver', 'Hennessy Prive', 'Maison Louis', 'Ardmore', 'Smirnoff', 'Glenmorangie 10YO', 'Hine XO', 'Cocktails', 'Montezuma', 'Matsui', 'Ciroc', 'Nikka Taketsuru', 'Napkin Holder', 'Krug Grande', "Hakushu Distiller's", 'Archers', 'Chandon', 'Courvoisier', 'Dalwhinnie 15YO', 'Glenfarclas 15YO', 'Moet', 'Pinnacle', 'Martell XO', 'Olmeca Reposado', 'Malibu', 'Demo Bundle', 'Kronenbourg 1664', 'Wuliangye Mellow', 'Johnnie Walker', 'Mortlach', 'Matsui Kurayoshi', 'Matsui Umeshu', "Maker's Mark", 'Copper', "Teacher's", 'Highland', 'Glen', 'Chandon Brut', 'Terrazas', 'Bottega Gold', "Gordon's Pink", 'Absolut Kurant', 'John Jameson', 'Glenfarclas 17YO', 'Absolut Peach', 'Matsui The', 'John', 'Patron Roca', 'Mortlach 16YO', 'Ruinart Rose', 'Tanqueray', 'Golden Glass', 'Copper Dog', 'Ketel One', 'Aberlour 12YO', 'Hennessy VSOP', 'Chivas', 'di', 'Chateau Latour', 'Maison', 'Martell Noblige', 'Glenfarclas 40YO', 'Hibiki 17YO', "Ballantine's 30YO", 'Lagavulin 16YO', 'Glenkinchie', 'Glenmorangie 14YO', 'Jinro Chamisul', 'Patron Anejo', 'Royal Lochnagar', 'Mumm Cordon', 'Bowmore 25YO', 'Caol ILA', 'Dame De', 'Asahi', 'Corona', 'Yamazaki', 'Condiments Long', 'Clynelish 14YO', 'Jura', "Ballantine's", 'Rail Square', 'Wuliangye', 'The Dalmore', 'Terrazas Altos', 'Havana', 'Jinro Strawberry', 'Bottega Soave', 'Chivas Regal', 'Ruinart', 'Paulaner Weissbier', 'Chateau', 'Ardbeg', 'Casamigos Joven', 'Carlsberg Danish', 'Cocktails by', "Gilbey's", 'Chateau Chauvin', 'Patron', 'Ardbeg 10YO', 'Patron XO', 'Saratoga', 'Campo', 'Crystal', 'Perrier', 'Smirnoff Red', 'Don', 'Paulaner', 'Aberlour', 'Casamigos Reposado', 'Chateau Pichon', 'Malesan Medoc', 'Rocks Glass', 'Casamigos', 'Jinro', 'Bottega Poeti', "Jacob's Creek", 'Cardhu', 'Dame', 'Monkey 47', 'Glenfarclas', 'Jura 18YO', 'Altos Blanco', 'Bottega 0', 'Wine', "Fleischmann's", 'Jinro Plum', 'Somersby Cider', 'Hine', 'Paulaner Munich', 'Absolut Elyx', 'El Recuerdo', 'Talisker 18YO', 'Ron', 'Black', 'Glenfarclas 30YO', 'Matsui Mizunara', 'Ardbeg Corryvreckan', 'Bowmore 12', 'Olmeca', 'Hennessy XO', 'Patron Citronge', 'Rain', 'Graffigna Pinot', 'Bacardi Superior', 'Bulleit', 'McCormick Orange', 'Balvenie', 'Dom Perignon', 'Passport', 'Cantenac Brown', 'Whisky Glass', 'Somersby', 'Krug', 'Glenfarclas 25YO', 'Patron Shot', '99', 'Cocktail', 'Cape', 'Alter', 'Terrazas Reserva', 'Ruinart R', 'Malesan Rouge', 'Royal Dragon', 'Bottega Stardust', 'Cutty Sark', 'Havana Club', 'Martell Chanteloup', 'McCormick Raspberry', 'Mumm Rose', 'McCormick Vanilla', 'Tanqueray Sevilla', 'Tanqueray Rangpur', 'J&B Rare', 'Tanqueray Ten', 'Cafe De', 'Aberlour 16YO', 'Hennessy', 'Jagermeister', 'Chateau Pedesclaux', 'Glenmorangie', 'Golden', 'Cutty', 'Bottega Rose', 'St', 'Carlsberg', 'Altos', 'Tequila', 'Rail Rectangular', 'The', 'Cragganmore 12YO', 'Campo Viejo', 'Belvedere Pink', 'Beefeater', 'Pernod', 'Paulaner Oktoberfest', 'Chateau Du', 'Nikka Coffey', 'Aberlour 18YO', 'Jack DanielÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¾ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢s', 'Label 5', 'Cantenac', 'Jura Seven', 'Black Velvet', 'Martell Cordon', 'Naked Grouse', 'Perrier Jouet', 'Penfolds Grange', "Ballantine's 12YO", 'Altos Reposado', 'McCormick Apple', "Teacher's Origin", 'Jura 12YO', 'Rocks', 'Absolut', 'Absolut Citron', 'Glen Grant', 'Dom', 'Penfolds Bin', 'Bulleit Rye', 'Cup', 'Baileys Cream', "Ballantine's 21YO", 'Glenkinchie 12YO', 'Tequila Rose', 'Monte', 'di Amore', 'Cutting', 'Absolut Original', 'Larios', 'Chateau Coutet', 'Martini Alta', 'Diesel', 'Chandon Rose', "Jacob's", 'Auchentoshan 12YO', 'Hibiki', 'Oban', 'Matsui Tottori', 'Jinro Grapefruit', 'Corona Extra', 'Hennessy Paradis', 'Barton', "Ballantine's Finest", 'Ricard', 'Caol', 'Montezuma Triple', 'Clynelish', 'McCormick', 'Jim Beam', 'Chateau Clos', 'Singleton', 'Crystal Head', 'Cardhu 12YO', "Fleischmann's Vanilla", 'Glenfarclas 12YO', 'Belvedere Pure', 'Glenmorangie 12YO', 'Ultimat', 'Ice Bucket', 'Yamazaki 18YO', 'Alter Ego', 'Mumm Blanc', 'Jose Cuervo', 'Balvenie 40YO', 'Martell NCF', 'Absolut Vanilia', 'Bacardi', 'Cloudy', "Mackinlay's", 'Glenrothes Vintage', "Broker's", 'El', 'Penfolds', 'Hibiki 21YO', 'Jim', 'Lagavulin', 'Martell VSOP', 'Montezuma Gold', 'Malibu Coconut', 'Mortlach 20YO', 'Wine Opener', 'Cutting Board', 'Cloudy Bay', 'Archers Peach', 'Oban 14YO', 'Johnnie', 'Jack', 'Bottega Petalo', 'Nikka', 'Ardbeg Uigeadail']

print("--------------------------------------------")

print("Web Scrapper Started Successfully ...")
ct = datetime.datetime.now()
print("Start Time :-", ct)

print("--------------------------------------------")

CHROMEDRIVER_PATH = '/usr/bin/chromedriver'

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)


# ------------------------------------------

# All Functions -

#-------------------------------------------------------------------------------------

# Functions for Site 1 - "https://cellarbration.com.sg/" -

def age_verification_1():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="agree-button"]')))
    driver.find_element(By.XPATH, '//button[@class="agree-button"]').click()
    time.sleep(5)


def get_links_1():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="product-item-link"]'))
        )
    except:
        print("Element not found !")

    for dt1 in productList:
        ld1 = dt1.get_property("href")
        print(ld1)
        productLinks_1.append(ld1)


def get_info_1(url):
    driver.get(url)

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[1]/h1/span'))
        )
        productName2  = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[4]/td').text.replace("ml", "").replace("8 X ", "").replace("4cans x ", "").replace("4 x ", "")
        volume = int(volume_tc) / 10
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[5]/td').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[3]/div[1]/span[2]/span/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '// *[ @ id = "product-price-2876"] / span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Cellarbration",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_1.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 2 - "https://cellarbration.com.sg/" -

def age_verification_2():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-radio-2"]/label/div[2]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="mat-button"]')))
    driver.find_element(By.XPATH, '//*[@id="mat-radio-2"]/label/div[2]').click()
    e = driver.find_element(By.XPATH, '//button[@class="mat-button"]')
    loc = e.location
    print(loc)
    elem = driver.find_element(By.XPATH, '//button[@class="mat-button"]')
    ac = ActionChains(driver)
    ac.move_by_offset(434, 435).click().perform()
    time.sleep(5)


def get_links_2():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/app-root/div/app-search/div/div/div/div[2]/div[2]/div/app-product-tile/div/div[1]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_2.append(ld1)
    except:
        print("Products are Sold Out")

    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/app-root/div/app-search/div/div/div/div[2]/div[2]/div/app-product-tile/div/div[2]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_2.append(ld1)
    except:
        print("Products are Available")


def get_info_2(url):
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
            EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/h4'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = productName2.replace("cl", "").split(" ")
        volume = volume_tc[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/p[1]').text
        catagory = catagory.split(",") and catagory.split(" ")
        catagory = catagory[1]
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/h3').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '// *[ @ id = "product-price-2876"] / span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "alcohaul",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_2.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 3 - "https://cellarbration.com.sg/" -

def age_verification_3():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="validation_yes"]')))
    driver.find_element(By.XPATH, '//*[@id="validation_yes"]').click()


def get_links_3():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="product-image image-container relative"]'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_3.append(ld1)
    except:
        print("Products not found !")


def get_info_3(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/h3'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = productName2.replace("cl", "").split(" ")
        # volume = volume_tc[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/p[1]').text
        catagory = catagory.split(",") and catagory.split(" ")
        catagory = catagory[1]
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/ul[2]/li/div').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '// *[ @ id = "product-price-2876"] / span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "alcoholporter",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_3.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 4 - "https://cellarbration.com.sg/" -

def age_verification_4():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalWine"]/div/div/div/div[1]/div/div[1]/div/form/input')))
    driver.find_element(By.XPATH, '//*[@id="modalWine"]/div/div/div/div[1]/div/div[1]/div/form/input').click()


def get_links_4():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="product-image image-container relative"]'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_4.append(ld1)
    except:
        print("Products not found !")


def get_info_4(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[2]/h3'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = productName2.replace("cl", "").replace("ml", "").split(" ")
        volume = volume_tc[-1]
        try:
            volume = int(volume) / 10
        except:
            volume = volume_tc[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li/div').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Bottels & Bottels",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_4.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 5 - "https://cellarbration.com.sg/" -s

def get_links_5():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="product-image "]'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_5.append(ld1)
    except:
        print("Products not found !")


def get_info_5(url):
    driver.get(url)

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-page"]/div[2]/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/p').text.replace("ml", "").replace("8 X ", "").replace("4cans x ", "").replace("4 x ", "")
        volume = int(volume_tc) / 10
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/div[4]/span/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/div[1]/div[1]/span').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/div[1]/div[1]/ins/span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "chuansenghuat",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_5.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 6 - "https://cellarbration.com.sg/" -

def age_verification_6():
    wait = WebDriverWait(driver, 300)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_links_6():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="items_list"]/div[2]/div/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_6.append(ld1)
    except:
        print("Products not found !")


def get_info_6(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-info-content"]/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="data-size"]').text.replace("CTL", "")
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="product-info-content"]/div[2]/div').text
        price = price.replace("$", "")
    except:
        print("Price not found for - ", url)

    tempV = {
        "Site": "coldstorage",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_6.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 7 - "https://cellarbration.com.sg/" -

def age_verification_7():
    wait = WebDriverWait(driver, 300)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_links_7():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/section[3]/div/div/div[4]/div/div[3]/div/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_7.append(ld1)
    except:
        print("Products not found !")


def get_info_7(url):
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
            EC.presence_of_element_located((By.XPATH, '/html/body/section[3]/div/div/div[2]/div[1]/h3'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div[7]/div[1]/div[1]/div/div[11]').text
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div[7]/div[1]/div[1]/div/div[5]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div[3]/div[1]/div[1]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="amount"]').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "cornerstonewines",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_7.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 8 - "https://cellarbration.com.sg/" -

def age_verification_8():
    wait = WebDriverWait(driver, 300)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_links_8():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="product-grid"]/div/div/div[1]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_8.append(ld1)
    except:
        print("Products not found !")


def get_info_8(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        pass
        # volume_1 = productName2.split(" ")
        # volume = volume_1[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[5]/div/div[1]/div/span').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="amount"]').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "getit",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_8.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 9 - "https://cellarbration.com.sg/" -

def age_verification_9():
    wait = WebDriverWait(driver, 300)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_links_9():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="items_list"]/div[2]/div/div/div[2]/div[2]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_9.append(ld1)
    except:
        print("Products not found !")


def get_info_9(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-info-content"]/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="data-size"]').text
        volume = volume.replace("CTL", "")
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[5]/div/div[1]/div/span').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="product-info-content"]/div[2]/div').text
        price = price.replace("$", "")
    except:
        print("Price not found for - ", url)

    tempV = {
        "Site": "giant",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_9.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 10 - "https://cellarbration.com.sg/" -

def age_verification_10():
    wait = WebDriverWait(driver, 300)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="close-icon"]')))
    driver.find_element(By.XPATH, '//*[@id="close-icon"]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agp_row"]/div/div/div[3]/div/form[1]')))
    driver.find_element(By.XPATH, '//*[@id="agp_row"]/div/div/div[3]/div/form[1]').click()


def get_links_10():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="shopify-section-static-search"]/div[1]/div[1]/ul/li/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_10.append(ld1)
    except:
        print("Products not found !")


def get_info_10(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[2]/td[2]').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[4]/td[2]').text
    except:
        try:
            catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]/a').text
        except:
            print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH,
                                    '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div/div/div[4]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH,
                                        '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div/div/div[4]/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "The Liquor Shop",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_10.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 11 - "https://cellarbration.com.sg/" -

def age_verification_11():
    wait = WebDriverWait(driver, 300)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div[1]/div/div/div[1]/button')))
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/div/div[1]/button').click()


def get_links_11():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__next"]/div[4]/div[1]/div[1]/div[3]/div/div[1]/div[3]/div/div[2]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_11.append(ld1)
    except:
        print("Products not found !")


def get_info_11(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[4]/div[1]/div/div[1]/div[2]/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[2]/td[2]').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[4]/td[2]').text
    except:
        try:
            catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]/a').text
        except:
            print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//strong[@class="ProductPrice_offer-price__RNnoW ProductPrice_desktop__mjtHR"]').text
        price = price.replace("SG$", "")
    except:
        print("Price not found for - ", url)

    tempV = {
        "Site": "millesima",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_11.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 12 - "https://cellarbration.com.sg/" -

def age_verification_12():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div[1]/div/div/div[1]/button')))
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/div/div[1]/button').click()


def get_links_12():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[6]/div/div/div/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_12.append(ld1)
    except:
        print("Products not found !")


def get_info_12(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[3]/span/span'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[3]/div/span[1]/span').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            try:
                volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div/span[1]/span').text
            except:
                print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[1]/div[1]/a[4]').text
    except:
        try:
            catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]/a').text
        except:
            print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "NUTC",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_12.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 13 - "https://cellarbration.com.sg/" -

def age_verification_13():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="preview_img"]/div[1]/section/div/div[2]/div[1]/button')))
    driver.find_element(By.XPATH, '//*[@id="preview_img"]/div[1]/section/div/div[2]/div[1]/button').click()


def get_links_13():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="PageContainer"]/main/div/div/div/div[1]/div/div/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_13.append(ld1)
    except:
        print("Products not found !")


def get_info_13(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProductSection--product-template"]/div[4]/div[2]/div/h1'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[3]/div/span[1]/span').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[1]/div[1]/a[4]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="ProductPrice"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Oak & Barrel",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_13.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 14 - "https://cellarbration.com.sg/" -

def get_links_14():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class = "j2store-thumbnail-image"]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_14.append(ld1)
    except:
        print("Products not found !")


def get_info_14(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="akeeba-renderjoomla"]/div/div/div[1]/div[2]/h1'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[2]/td[2]/strong').text
        volume = int(volume)/10
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="akeeba-renderjoomla"]/div/div/div[1]/div[2]/div[2]/div[3]/div[1]/div').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "liquorbar",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_14.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 15 - "https://cellarbration.com.sg/" -

def age_verification_15():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wpforms-483-field_1_1"]')))
    driver.find_element(By.XPATH, '//*[@id="wpforms-483-field_1_1"]').click()
    driver.find_element(By.XPATH, '//*[@id="wpforms-submit-483"]').click()


def get_links_15():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="woof_results_by_ajax"]/ul/li/a[1]'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_15.append(ld1)
    except:
        print("Products not found !")


def get_info_15(url):
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
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[2]/h1'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="product-4216"]/div[2]/h1').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1]
    except:
        try:
            volume = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/p[2]/text()').text.replace("ml", "")
            # volume = int(volume)/10
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[2]/p/ins/span/bdi').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[2]/p/ins/span/bdi/text()').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "thirstydonkey",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_15.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 16 - "https://cellarbration.com.sg/" -

def age_verification_16():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popmake-278"]/div[2]/p[4]/button')))
    driver.find_element(By.XPATH, '//*[@id="popmake-278"]/div[2]/p[4]/button').click()


def get_links_16():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div/div/main/div/article/div/div/div[1]/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_16.append(ld1)
    except:
        print("Products not found !")


def get_info_16(url):
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
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/nav'))
        )
        productName2 = productName2.text
        productName_2 = productName2.split("/")
        productName2 = productName_2[-1]
    except:
        print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1]
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = productName_2[-2]
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/p[1]/ins/span/bdi').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/p/span/bdi').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "tyliquor",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_16.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 17 - "https://cellarbration.com.sg/" -

def age_verification_17():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalWine"]/div/div/div/div[2]/div/div/div/form/button[1]')))
    driver.find_element(By.XPATH, '//*[@id="modalWine"]/div/div/div/div[2]/div/div/div/form/button[1]').click()


def get_links_17():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[6]/div/div/div[2]/div/div/div[1]/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_17.append(ld1)
    except:
        print("Products not found !")


def get_info_17(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/div[1]'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div[2]/div/div[3]/div[1]/select/option').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div[2]/div/div[3]/div[1]/select/option').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/ul/li/div').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "winesnspirits",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_17.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 18 - "https://cellarbration.com.sg/" -

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

# Functions for Site 19 - "https://cellarbration.com.sg/" -

def age_verification_19():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agp_row"]/div/div/div[4]/div/form[1]/input')))
    driver.find_element(By.XPATH, '//*[@id="agp_row"]/div/div/div[4]/div/form[1]/input').click()


def get_links_19():
    try:
        productList = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="shopify-section-search-template"]/div/div/div/div/div/a'))
        )
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks_19.append(ld1)
    except:
        print("Products not found !")


def get_info_19(url):
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
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProductSection"]/div/div[2]/h1'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[2]').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/span').text
        volume = int(volume)/10
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="productPrice-product-template"]/span[1]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="productPrice-product-template"]/span[1]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "boozemart",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_19.append(tempV)

#-------------------------------------------------------------------------------------


# All Driver Codes -


# -------------------------------------------------------------------------------------

# Driver Code 1 -

# driver = webdriver.Chrome(ChromeDriverManager().install())  # For IDE (Uncomment in IDE)

site_name = ["https://cellarbration.com.sg/", "https://alcohaul.sg/", "https://www.alcoholporter.com/", "https://www.bnb.com.sg/", "https://chuansenghuat.com.sg/", "https://coldstorage.com.sg/", "https://shop.cornerstonewines.com/", "https://getit.changirecommends.com/", "https://giant.sg/", "https://www.theliquorshop.com.sg/", "https://www.millesima.sg/", "https://www.fairprice.com.sg/", "https://oakandbarrel.com.sg/", "https://www.liquorbar.sg/", "https://thirstydonkey.sg/", "https://www.tyliquor.sg/", "https://www.winesnspirits.sg/", "https://www.oaks.com.sg/", "https://boozemart.sg/"]

for sn in site_name:
    driver.get(sn)
    print(">> ", driver.title)

    if sn == "https://cellarbration.com.sg/":
        try:
            age_verification_1()
        except:
            print("Age verification failed")
        for productName in FinalProductNameList[0:5]:
            productName = productName.replace(" ", "%20")
            surl = "https://cellarbration.com.sg/catalogsearch/result/index/?product_list_limit=60&q=" + productName
            try:
                driver.get(surl)
                get_links_1()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_1)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_1.append(item)
        print(uniqueLnks_1)
        print(len(uniqueLnks_1))
        for lnk2 in uniqueLnks_1:
            get_info_1(lnk2)
            print("Final Data :- ", finalData_1[-1])
            print("No of Product Info. :- ", len(finalData_1))
            print(finalData_1[-1])
        clean_data_1 = [i for n, i in enumerate(finalData_1) if i not in finalData_1[n + 1:]]

    elif sn == "https://alcohaul.sg/":
        try:
            age_verification_2()
        except:
            print("Age verification  failed")
        for productName in FinalProductNameList[0:5]:
            surl = "https://alcohaul.sg/search?search=" + productName
            try:
                driver.get(surl)
                get_links_2()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_2)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_2.append(item)
        print(uniqueLnks_2)
        print(len(uniqueLnks_2))
        for lnk2 in uniqueLnks_2:
            get_info_2(lnk2)
            print("Final Data :- ", finalData_2[-1])
            print("No of Product Info. :- ", len(finalData_2))
            print(finalData_2[-1])
        clean_data_2 = [i for n, i in enumerate(finalData_2) if i not in finalData_2[n + 1:]]

    elif sn == "https://www.alcoholporter.com/":
        try:
            age_verification_3()
        except:
            print("Age verification  failed")
        for productName in FinalProductNameList[0:5]:
            surl = "https://www.alcoholporter.com/index.php?route=product/search&search=" + productName
            try:
                driver.get(surl)
                get_links_3()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_3)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_3.append(item)
        print(uniqueLnks_3)
        print(len(uniqueLnks_3))
        for lnk2 in uniqueLnks_3:
            get_info_3(lnk2)
            print("Final Data :- ", finalData_3[-1])
            print("No of Product Info. :- ", len(finalData_3))
            print(finalData_3[-1])
        clean_data_3 = [i for n, i in enumerate(finalData_3) if i not in finalData_3[n + 1:]]

    elif sn == "https://www.bnb.com.sg/":
        try:
            age_verification_4()
        except:
            print("Age verification  failed")
        for productName in FinalProductNameList[0:5]:
            surl = "https://www.bnb.com.sg/index.php?route=product/search&search=" + productName
            try:
                driver.get(surl)
                get_links_4()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_4)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_4.append(item)
        print(uniqueLnks_4)
        print(len(uniqueLnks_4))
        for lnk2 in uniqueLnks_4:
            get_info_4(lnk2)
            print("Final Data :- ", finalData_4[-1])
            print("No of Product Info. :- ", len(finalData_4))
            print(finalData_4[-1])
        clean_data_4 = [i for n, i in enumerate(finalData_4) if i not in finalData_4[n + 1:]]

    elif sn == "https://chuansenghuat.com.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://chuansenghuat.com.sg/?s=" + productName + "&post_type=product"
            try:
                driver.get(surl)
                get_links_5()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_5)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_5.append(item)
        print(uniqueLnks_5)
        print(len(uniqueLnks_5))
        for lnk2 in uniqueLnks_5:
            get_info_5(lnk2)
            print("Final Data :- ", finalData_5[-1])
            print("No of Product Info. :- ", len(finalData_5))
            print(finalData_5[-1])
        clean_data_5 = [i for n, i in enumerate(finalData_5) if i not in finalData_5[n + 1:]]

    elif sn == "https://coldstorage.com.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://coldstorage.com.sg/search?q=" + productName
            try:
                driver.get(surl)
                get_links_6()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_6)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_6.append(item)
        print(uniqueLnks_6)
        print(len(uniqueLnks_6))
        for lnk2 in uniqueLnks_6:
            get_info_6(lnk2)
            print("Final Data :- ", finalData_6[-1])
            print("No of Product Info. :- ", len(finalData_6))
            print(finalData_6[-1])
        clean_data_6 = [i for n, i in enumerate(finalData_6) if i not in finalData_6[n + 1:]]

    elif sn == "https://shop.cornerstonewines.com/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://shop.cornerstonewines.com/list.php?item_group=Wine%27+or+item_group%3D%27Spirit%27+or+item_group%3D%27Non-Alcoholics&submit_Lsearch=&serach_keyword=" + productName
            try:
                driver.get(surl)
                get_links_7()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_7)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_7.append(item)
        print(uniqueLnks_7)
        print(len(uniqueLnks_7))
        for lnk2 in uniqueLnks_7:
            get_info_7(lnk2)
            print("Final Data :- ", finalData_7[-1])
            print("No of Product Info. :- ", len(finalData_7))
            print(finalData_7[-1])
        clean_data_7 = [i for n, i in enumerate(finalData_7) if i not in finalData_7[n + 1:]]

    elif sn == "https://getit.changirecommends.com/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://getit.changirecommends.com/search/" + productName
            try:
                driver.get(surl)
                get_links_8()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_8)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_8.append(item)
        print(uniqueLnks_8)
        print(len(uniqueLnks_8))
        for lnk2 in uniqueLnks_8:
            get_info_8(lnk2)
            print("Final Data :- ", finalData_8[-1])
            print("No of Product Info. :- ", len(finalData_8))
            print(finalData_8[-1])
        clean_data_8 = [i for n, i in enumerate(finalData_8) if i not in finalData_8[n + 1:]]
    elif sn == "https://giant.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://giant.sg/search?q=" + productName
            try:
                driver.get(surl)
                get_links_9()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_9)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_9.append(item)
        print(uniqueLnks_9)
        print(len(uniqueLnks_9))
        for lnk2 in uniqueLnks_9:
            get_info_9(lnk2)
            print("Final Data :- ", finalData_9[-1])
            print("No of Product Info. :- ", len(finalData_9))
            print(finalData_9[-1])
        clean_data_9 = [i for n, i in enumerate(finalData_9) if i not in finalData_9[n + 1:]]

    elif sn == "https://www.theliquorshop.com.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://www.theliquorshop.com.sg/search?type=article%2Cpage%2Cproduct&q=" + productName
            try:
                driver.get(surl)
                get_links_10()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_10)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_10.append(item)
        print(uniqueLnks_10)
        print(len(uniqueLnks_10))
        for lnk2 in uniqueLnks_10:
            get_info_10(lnk2)
            print("Final Data :- ", finalData_10[-1])
            print("No of Product Info. :- ", len(finalData_10))
            print(finalData_10[-1])
        clean_data_10 = [i for n, i in enumerate(finalData_10) if i not in finalData_10[n + 1:]]

    elif sn == "https://www.millesima.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://www.millesima.sg/search?searchTerm=" + productName
            try:
                driver.get(surl)
                get_links_11()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_11)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_11.append(item)
        print(uniqueLnks_11)
        print(len(uniqueLnks_11))
        for lnk2 in uniqueLnks_11:
            get_info_11(lnk2)
            print("Final Data :- ", finalData_11[-1])
            print("No of Product Info. :- ", len(finalData_11))
            print(finalData_11[-1])
        clean_data_11 = [i for n, i in enumerate(finalData_11) if i not in finalData_11[n + 1:]]

    elif sn == "https://www.fairprice.com.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://www.fairprice.com.sg/search?query=" + productName
            try:
                driver.get(surl)
                get_links_12()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_12)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_12.append(item)
        print(uniqueLnks_12)
        print(len(uniqueLnks_12))
        for lnk2 in uniqueLnks_12:
            get_info_12(lnk2)
            print("Final Data :- ", finalData_12[-1])
            print("No of Product Info. :- ", len(finalData_12))
            print(finalData_12[-1])
        clean_data_12 = [i for n, i in enumerate(finalData_12) if i not in finalData_12[n + 1:]]

    elif sn == "https://oakandbarrel.com.sg/":
        try:
            age_verification_13()
        except:
            print("Age verification failed !")

        for productName in FinalProductNameList[0:5]:
            surl = "https://oakandbarrel.com.sg/search?q=" + productName
            try:
                driver.get(surl)
                get_links_13()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_13)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_13.append(item)
        print(uniqueLnks_13)
        print(len(uniqueLnks_13))
        for lnk2 in uniqueLnks_13:
            get_info_13(lnk2)
            print("Final Data :- ", finalData_13[-1])
            print("No of Product Info. :- ", len(finalData_13))
            print(finalData_13[-1])
        clean_data_13 = [i for n, i in enumerate(finalData_13) if i not in finalData_13[n + 1:]]

    elif sn == "https://www.liquorbar.sg/":
        for productName in FinalProductNameList[0:5]:
            surl = "https://www.liquorbar.sg/index.php/products?search=" + productName + "&catid%5B0%5D=84&catid%5B1%5D=97&catid%5B2%5D=178&catid%5B3%5D=179&catid%5B4%5D=180"
            try:
                driver.get(surl)
                get_links_14()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_14)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_14.append(item)
        print(uniqueLnks_14)
        print(len(uniqueLnks_14))
        for lnk2 in uniqueLnks_14:
            get_info_14(lnk2)
            print("Final Data :- ", finalData_14[-1])
            print("No of Product Info. :- ", len(finalData_14))
            print(finalData_14[-1])
        clean_data_14 = [i for n, i in enumerate(finalData_14) if i not in finalData_14[n + 1:]]

    elif sn == "https://thirstydonkey.sg/":
        try:
            age_verification_15()
        except:
            print("Age verification failed !")

        for productName in FinalProductNameList[0:5]:
            surl = "https://thirstydonkey.sg/?s=" + productName + "&post_type=product&dgwt_wcas=1"
            try:
                driver.get(surl)
                get_links_15()
            except:
                try:
                    driver.get(surl)
                    get_info_15(surl)
                except:
                    print("No product found for search - ", surl)
        a = set(productLinks_15)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_15.append(item)
        print(uniqueLnks_15)
        print(len(uniqueLnks_15))
        for lnk2 in uniqueLnks_15:
            get_info_15(lnk2)
            print("Final Data :- ", finalData_15[-1])
            print("No of Product Info. :- ", len(finalData_15))
            print(finalData_15[-1])
        clean_data_15 = [i for n, i in enumerate(finalData_15) if i not in finalData_15[n + 1:]]

    elif sn == "https://www.tyliquor.sg/":
        try:
            age_verification_16()
        except:
            print("Age verification failed !")

        for productName in FinalProductNameList[0:5]:
            surl = "https://www.tyliquor.sg/?s=" + productName
            try:
                driver.get(surl)
                get_links_16()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_16)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_16.append(item)
        print(uniqueLnks_16)
        print(len(uniqueLnks_16))
        for lnk2 in uniqueLnks_16:
            get_info_16(lnk2)
            print("Final Data :- ", finalData_16[-1])
            print("No of Product Info. :- ", len(finalData_16))
            print(finalData_16[-1])
        clean_data_16 = [i for n, i in enumerate(finalData_16) if i not in finalData_16[n + 1:]]

    elif sn == "https://www.winesnspirits.sg/":
        try:
            age_verification_17()
        except:
            print("Age verification failed !")

        for productName in FinalProductNameList[0:5]:
            surl = "https://www.winesnspirits.sg/index.php?route=product/search&search=" + productName
            try:
                driver.get(surl)
                get_links_17()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_17)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_17.append(item)
        print(uniqueLnks_17)
        print(len(uniqueLnks_17))
        for lnk2 in uniqueLnks_17:
            get_info_17(lnk2)
            print("Final Data :- ", finalData_17[-1])
            print("No of Product Info. :- ", len(finalData_17))
            print(finalData_17[-1])
        clean_data_17 = [i for n, i in enumerate(finalData_17) if i not in finalData_17[n + 1:]]

    elif sn == "https://www.oaks.com.sg/":
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

    elif sn == "https://boozemart.sg/":
        try:
            age_verification_19()
        except:
            print("Age verification failed !")

        for productName in FinalProductNameList[0:5]:
            surl = "https://boozemart.sg/search?type=product&q=" + productName
            try:
                driver.get(surl)
                get_links_19()
            except:
                print("No product found for search - ", surl)
        a = set(productLinks_19)
        a = list(set(a))
        seen = set()
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                uniqueLnks_19.append(item)
        print(uniqueLnks_19)
        print(len(uniqueLnks_19))
        for lnk2 in uniqueLnks_19:
            get_info_19(lnk2)
            print("Final Data :- ", finalData_19[-1])
            print("No of Product Info. :- ", len(finalData_19))
            print(finalData_19[-1])
        clean_data_19 = [i for n, i in enumerate(finalData_19) if i not in finalData_19[n + 1:]]
    else:
        driver.close()

# Final Processing -

clean_data = [*clean_data_1, *clean_data_2, *clean_data_3, *clean_data_4, *clean_data_5, *clean_data_6, *clean_data_7, *clean_data_8, *clean_data_9, *clean_data_10, *clean_data_11, *clean_data_12, *clean_data_13, *clean_data_14, *clean_data_15, *clean_data_16, *clean_data_17, *clean_data_18, *clean_data_19]
print(clean_data)
print(len(clean_data))

# Data Saving -

# Saving the Data to Excel Sheet -

df = pd.DataFrame.from_dict(clean_data)
print(df)
df.to_excel('finalData.xlsx', index=False)

# To Save Data in JSON file -
import json


def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data(title):
    with open(title, encoding="utf-8") as f:
        return json.load(f)


save_data("finalData.json", clean_data)

# ........................................................................................

# To Store Scraped Data in MYSQL Database (Remote Database) -
try:
    engine = create_engine("mysql+pymysql://adam:password@localhost/uddipan")
    df = pd.read_json("finalData.json")
    df.to_sql("Product_prices", con=engine, if_exists="replace", index=False)
    print("Data updated in Database...")
except:
    print(">> Cannot Connect to Database")

# ........................................................................................


print("--------------------------------------------")
ct1 = datetime.datetime.now()
print("Start Time :-", ct)
print("End Time :-", ct1)
print("--------------------------------------------")
