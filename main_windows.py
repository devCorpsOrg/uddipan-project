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

productNamesList = ["99 Schnapps Bananas", "99 Schnapps Apple", "99 Schnapps Blackberries", "99 Schnapps Orange",
                    "Aberlour 12YO Double Cask", "Aberlour 16YO", "Aberlour 18YO", "Absolut Citron",
                    "Absolut Elyx Flare", "Absolut Extrakt", "Absolut Kurant", "Absolut Mandrin", "Absolut Original",
                    "Absolut Original", "Absolut Original", "Absolut Original", "Absolut Original",
                    "Absolut Original 24Hours Delivery", "Absolut Peach", "Absolut Vanilia", "Absolut Vanilia",
                    "Absolut Vanilia", "Absolut Vanilia 24 Hour Delivery", "Alexander Society Flute Glass",
                    "Alter Ego De Palmer 2013 Margaux AOC", "Altos Blanco", "Altos Reposado", "Archers Peach Schnapps",
                    "Ardbeg 10YO", "Ardbeg Corryvreckan", "Ardbeg Uigeadail", "Ardmore", "Asahi Super Dry",
                    "Asahi Super Dry Black", "Auchentoshan 12YO Triple Distilled", "Auchentoshan 12YO Triple Distilled",
                    "Bacardi Superior", "Baileys Cream", "Baileys Cream", "Ballantine's 12YO", "Ballantine's 17YO",
                    "Ballantine's 21YO", "Ballantine's 30YO", "Ballantine's Finest", "Balvenie 40YO", "Barton",
                    "Barton", "Beefeater", "Beefeater 24", "Belvedere Pink Grapefruit", "Belvedere Pure",
                    "Black & White", "Black & White", "Black & White", "Black Velvet", "Black Velvet", "Bottega 0 Rose",
                    "Bottega Fragolino Rosso Party", "Bottega Gold Prosecco", "Bottega Petalo Amore",
                    "Bottega Petalo Amore", "Bottega Poeti Prosecco Spumante Brut",
                    "Bottega Poeti Prosecco Spumante Brut", "Bottega Rose Brut", "Bottega Rose Gold",
                    "Bottega Soave Classico DOC", "Bottega Stardust No Liquid", "Bottega Stardust No Liquid",
                    "Bottega Stardust Prosecco DOC", "Bowmore 12 YO & 18 YO", "Bowmore 12YO", "Bowmore 18YO",
                    "Bowmore 25YO", "Brancott Estate Letter 'B' Sauvignon Blanc",
                    "Brancott Estate Letter 'T' Pinot Noir", "Brancott Estate Marlborough Sauvignon Blanc",
                    "Brancott Estate Pinot Noir", "Broker's", "Bulleit", "Bulleit Rye", "Cafe De Paris",
                    "Cafe De Paris Lychee", "Cafe De Paris Peach", "Campo Viejo Tempranillo", "Campo Viejo Viura",
                    "Cantenac Brown 2018 Margaux AOC", "Caol ILA 12YO", "Cape Mentelle Cabernet Merlot",
                    "Cape Mentelle Chardonnay", "Cape Mentelle Sauvignon Blanc Semillon", "Cape Mentelle Shiraz",
                    "Captain Morgan Dark", "Captain Morgan Spiced Gold", "Captain Morgan White", "Cardhu 12YO",
                    "Carlsberg Danish Pilsner", "Casamigos Anejo", "Casamigos Blanco", "Casamigos Joven",
                    "Casamigos Reposado", "Chandon Brut Non Vintage", "Chandon Brut Non Vintage",
                    "Chandon Rose Non Vintage", "Chateau Chauvin 2016 St-Emilion Grand Cru",
                    "Chateau Clos Floridene 2018 Graves Rouge AOC", "Chateau Coutet 2017 Barsac AOC",
                    "Chateau Coutet 2018 Barsac AOC", "Chateau D'Armailhac 2017 Pauillac AOC",
                    "Chateau Du Tertre 2018 Margaux AOC", "Chateau Fonreaud 2011 Listrac-Medoc AOC",
                    "Chateau Lafon Rochet 2011 St-Estephe AOC", "Chateau Latour Carnet 2016 Haut-Medoc AOC",
                    "Chateau Pedesclaux 2017 Pauillac AOC", "Chateau Pichon Baron 2014 Pauillac AOC",
                    "Chivas Regal 12YO", "Chivas Regal 12YO", "Chivas Regal 12YO", "Chivas Regal 12YO",
                    "Chivas Regal 12YO", "Chivas Regal 18YO", "Chivas Regal 18YO", "Chivas Regal 18YO",
                    "Chivas Regal 18YO + 12YO", "Chivas Regal 18YO + 12YO 24 Hour Delivery", "Chivas Regal 25YO",
                    "Chivas Regal Extra", "Chivas Regal Extra 13YO American Rye",
                    "Chivas Regal Extra 13YO American Rye + Sherry Cask", "Chivas Regal Extra 13YO Sherry Cask",
                    "Chivas Regal Mizunara", "Chivas Regal XV Gold 15YO", "Chivas Regal XV Gold 15YO", "Ciroc",
                    "Cloudy Bay Chardonnay", "Cloudy Bay Pinot Noir", "Cloudy Bay Sauvignon Blanc",
                    "Cloudy Bay Sauvignon Blanc", "Cloudy Bay Te Koko", "Clynelish 14YO", "Cocktail Shaker",
                    "Cocktails by Jenn Lemon Drop", "Condiments Long Tray", "Copper Dog", "Corona Extra",
                    "Corona Extra 24Hours Delivery", "Courvoisier Premier Reserve", "Courvoisier VSOP Napoleon",
                    "Courvoisier XO", "Cragganmore 12YO", "Crystal Head", "Crystal Head",
                    "Crystal Head Original Bottle No Liquid", "Crystal Head Skull Stem Martini Glass", "Cup Shot",
                    "Cutting Board", "Cutty Sark", "Dalwhinnie 15YO", "Dame De Bouard 2018 Montagne-St-Emilion AOC",
                    "Demo Bundle Product", "di Amore Amaretto", "di Amore Quattro Orange", "di Amore Raspberry",
                    "di Amore Sambucca", "Diesel 190 Proof", "Diesel 190 Proof 24Hours Delivery",
                    "Dom Perignon Rose Vintage 2006", "Dom Perignon Vintage 2010", "Don Julio 1942", "Don Julio Anejo",
                    "Don Julio Blanco", "Don Julio Reposado", "Don Julio Reposado", "El Recuerdo de Oaxaca",
                    "El Recuerdo de Oaxaca", "Fleischmann's Vanilla", "Fugue De Nenin 2018 Pomerol AOC", "Gilbey's",
                    "Glen Grant 10YO", "Glen Grant 12YO", "Glen Grant 15YO", "Glen Grant 18YO", "Glenfarclas 12YO",
                    "Glenfarclas 15YO", "Glenfarclas 15YO 24Hours Delivery", "Glenfarclas 17YO",
                    "Glenfarclas 17YO 24 Hour Delivery", "Glenfarclas 21YO", "Glenfarclas 25YO", "Glenfarclas 30YO",
                    "Glenfarclas 40YO", "Glenkinchie 12YO", "Glenmorangie 10YO Original",
                    "Glenmorangie 12YO The Lasanta", "Glenmorangie 14YO Quinta Ruban", "Glenmorangie 18YO Extra Rare",
                    "Glenmorangie Nectar d'Or Rare Cask", "Glenmorangie Signet", "Glenrothes Vintage 1985",
                    "Golden Glass", "Gordon's", "Gordon's", "Gordon's", "Gordon's", "Gordon's", "Gordon's Pink",
                    "Graffigna Pinot Grigio Reserve", "Hakushu Distiller's Reserve", "Havana Club 3YO",
                    "Havana Club 7YO", "Hennessy Paradis", "Hennessy Prive", "Hennessy Richard", "Hennessy VSOP",
                    "Hennessy VSOP", "Hennessy XO", "Hennessy XO", "Hibiki 17YO", "Hibiki 21YO Mount Fuji Ltd Edition",
                    "Highland Mist", "Highland Mist", "Hine XO", "Ice Bucket Black", "Ice Bucket Blue",
                    "Ice Bucket Stainless Steel", "Ice Bucket Transparent", "J&B Rare",
                    "Jack DanielÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢s Honey",
                    "Jack DanielÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾Ãƒâ€šÃ‚Â¢s Old No. 7",
                    "Jacob's Creek Cabernet Sauvignon", "Jacob's Creek Chardonnay", "Jacob's Creek Chardonnay",
                    "Jacob's Creek Chardonnay Pinot Noir", "Jacob's Creek Dots Moscato",
                    "Jacob's Creek Dots Moscato Rose", "Jacob's Creek Double Barrel Cabernet Sauvignon",
                    "Jacob's Creek Double Barrel Shiraz", "Jacob's Creek Grenache Shiraz", "Jacob's Creek Merlot",
                    "Jacob's Creek Reserve Cabernet Sauvignon", "Jacob's Creek Reserve Chardonnay",
                    "Jacob's Creek Reserve Riesling", "Jacob's Creek Reserve Shiraz", "Jacob's Creek Riesling",
                    "Jacob's Creek Rose", "Jacob's Creek Sauvignon Blanc", "Jacob's Creek Shiraz",
                    "Jacob's Creek Shiraz Cabernet", "Jacob's Creek Shiraz Cabernet",
                    "Jacob's Creek Twin Pickings Pinot Gris", "Jacob's Creek Twin Pickings Sauvignon Blanc",
                    "Jagermeister", "Jim Beam White", "Jim Beam White", "Jinro Chamisul Fresh",
                    "Jinro Flavour 10xGrapefruit 10xStrawberry", "Jinro Flavour 10xPlum 10xGrapefruit",
                    "Jinro Flavour 10xStrawberry 10xPlum", "Jinro Flavour 1xGrapefruit 1xPlum 2x Strawberry",
                    "Jinro Flavour 3xGrapefruit 3xPlum 2xStrawberry", "Jinro Flavour 3xGrapefruit 3xPlum 4xStrawberry",
                    "Jinro Grapefruit", "Jinro Plum", "Jinro Strawberry", "John Jameson Standard",
                    "John Jameson Standard", "Johnnie Walker 18YO", "Johnnie Walker Black Label",
                    "Johnnie Walker Black Label", "Johnnie Walker Black Label", "Johnnie Walker Black Label",
                    "Johnnie Walker Blue Label", "Johnnie Walker Double Black", "Johnnie Walker Gold Label Reserve",
                    "Johnnie Walker Green Label 15YO", "Johnnie Walker Red Label", "Johnnie Walker Red Label",
                    "Johnnie Walker Red Label", "Johnnie Walker Red Label", "Johnnie Walker Red Label",
                    "Johnnie Walker Red Label", "Johnnie Walker White Walker", "Johnnie Walker White Walker",
                    "Johnnie Walker XR21", "Jose Cuervo", "Jose Cuervo", "Jose Cuervo Shot Glass", "Jura 12YO",
                    "Jura 18YO", "Jura Seven Wood", "Kahlua Coffee", "Ketel One Citroen", "Ketel One Original",
                    "Kronenbourg 1664 Blanc", "Kronenbourg 1664 Lager", "Krug Grande Cuvee Non Vintage",
                    "Krug Vintage 2006", "Label 5 Classic Black", "Lagavulin 16YO", "Larios", "Mackinlay's Shackleton",
                    "Maison Louis Girard Coteaux 2019 Burgundy AOC", "Maison Louis Girard Pinot Noir 2020 Burgundy AOC",
                    "Maker's Mark", "Malesan Blanc 2019 VDT", "Malesan Blanc 2019 VDT", "Malesan Blanc 2019 VDT",
                    "Malesan Medoc 2019 AOC", "Malesan Rouge 2019 Bordeaux Terra Vitis AOC", "Malesan Rouge 2020 VDT",
                    "Malesan Rouge 2020 VDT", "Malesan Rouge 2020 VDT", "Malibu Coconut Rum", "Martell Chanteloup XXO",
                    "Martell Cordon Bleu", "Martell Cordon Bleu", "Martell Cordon Bleu", "Martell Cordon Bleu (Cradle)",
                    "Martell Cordon Bleu (Cradle)", "Martell Cordon Bleu Prestige Ltd Edition", "Martell NCF",
                    "Martell Noblige", "Martell VSOP Red Barrel", "Martell VSOP Red Barrel", "Martell VSOP Red Barrel",
                    "Martell VSOP Red Barrel (Cradle)", "Martell XO", "Martini Alta Langa", "Matsui Kurayoshi",
                    "Matsui Kurayoshi 12YO", "Matsui Kurayoshi 18 YO", "Matsui Kurayoshi 25YO", "Matsui Kurayoshi 33YO",
                    "Matsui Kurayoshi 8YO", "Matsui Kurayoshi Sherry Cask", "Matsui Mizunara Cask", "Matsui Sakura",
                    "Matsui San-In", "Matsui The Peated", "Matsui Tottori", "Matsui Tottori 17YO",
                    "Matsui Tottori 21YO", "Matsui Tottori 23YO", "Matsui Tottori 27YO",
                    "Matsui Tottori Bourbon Barrel", "Matsui Umeshu Brandy", "Matsui Umeshu Whisky", "McCormick Apple",
                    "McCormick Orange", "McCormick Raspberry", "McCormick Vanilla",
                    "Moet & Chandon Imperial Non Vintage", "Moet & Chandon Imperial Non Vintage",
                    "Moet & Chandon Imperial Non Vintage", "Moet & Chandon Imperial Rose Non Vintage", "Monkey 47 Dry",
                    "Monkey 47 Sloe", "Monte Alban", "Montezuma Gold", "Montezuma Gold", "Montezuma Gold",
                    "Montezuma Gold", "Montezuma Silver", "Montezuma Silver", "Montezuma Silver", "Montezuma Silver",
                    "Montezuma Triple Sec", "Mortlach 12YO", "Mortlach 16YO", "Mortlach 20YO",
                    "Mumm Blanc de Blancs Non Vintage", "Mumm Cordon Rouge Non Vintage",
                    "Mumm Cordon Rouge Non Vintage", "Mumm Rose Non Vintage", "Naked Grouse", "Naked Grouse",
                    "Napkin Holder", "Nikka Coffey Japan", "Nikka Coffey Japan", "Nikka From the Barrel",
                    "Nikka From the Barrel", "Nikka Super Rare Old", "Nikka Taketsuru", "Nikka Taketsuru 17YO",
                    "Nikka Taketsuru 21YO", "Oban 14YO", "Olmeca Reposado", "Passport", "Patron Anejo", "Patron Anejo",
                    "Patron Citronge Orange", "Patron Reposado", "Patron Reposado", "Patron Roca Anejo",
                    "Patron Roca Reposado", "Patron Shot Glass", "Patron Silver", "Patron Silver",
                    "Patron Silver Bee Ltd Edition", "Patron XO Cafe",
                    "Patron XO CafÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©", "Patron XO Cafe Dark Cocoa",
                    "Patron XO CafÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© Dark Cocoa", "Paulaner Munich Hell Lager",
                    "Paulaner Munich Hell Lager", "Paulaner Oktoberfest Marzen", "Paulaner Weissbier Dunkel Dark Wheat",
                    "Paulaner Weissbier Wheat", "Penfolds Bin 128 Coonawarra Shiraz 2018",
                    "Penfolds Bin 2 Shiraz Mataro 2019", "Penfolds Bin 28 Kalimna Shiraz",
                    "Penfolds Bin 389 Cabernet Shiraz 2016", "Penfolds Bin 407 Cabernet Sauvignon 2019",
                    "Penfolds Bin 8 Cabernet Shiraz 2019", "Penfolds Grange Bin 95 Shiraz 2013", "Pernod",
                    "Perrier Jouet Belle Epoque Rose Vintage 2012", "Perrier Jouet Belle Epoque Vintage 2013",
                    "Perrier Jouet Blason Rose Non Vintage", "Perrier Jouet Grand Brut Non Vintage", "Pimm's Aperitif",
                    "Pinnacle", "Rail Rectangular Mat", "Rail Square Mat", "Rain Organics Cucumber Lime",
                    "Rain Organics Cucumber Lime", "Rain Organics Lavender Lemonade", "Rain Organics Original",
                    "Rain Organics Original", "Rain Organics Red Grape Hibiscus", "Rain Organics Red Grape Hibiscus",
                    "Ricard", "Rocks Glass", "Ron Zacapa Sistema Solera Centenario 23",
                    "Ron Zacapa Solera Centenario XO", "Royal Dragon Superior", "Royal Lochnagar 12YO",
                    "Royal Salute 21YO", "Royal Salute 62 Gun", "Ruinart Blanc de Blancs Non Vintage",
                    "Ruinart R De Non Vintage", "Ruinart Rose Non Vintage", "Saratoga Dark", "Sauza Extra Gold",
                    "Sauza Extra Gold", "Singleton Dufftown 12YO", "Singleton Dufftown 12YO", "Singleton Dufftown 12YO",
                    "Singleton Dufftown 12YO & 15YO", "Singleton Dufftown 12YO 24Hours Delivery",
                    "Singleton Dufftown 15YO", "Singleton Dufftown 15YO", "Singleton Dufftown 18YO",
                    "Singleton Dufftown 18YO", "Smirnoff Black", "Smirnoff Red", "Smirnoff Red", "Smirnoff Red",
                    "Smirnoff Red Label", "Somersby Cider Apple", "Somersby Cider Pear",
                    "Somersby Cider Sparkling Rose", "St Hugo Cabernet Sauvignon", "St Hugo Shiraz", "Talisker 10YO",
                    "Talisker 18YO", "Tanqueray", "Tanqueray Rangpur", "Tanqueray Sevilla", "Tanqueray Ten",
                    "Tarantula Azul", "Tarantula Azul", "Teacher's Origin", "Teacher's Origin",
                    "Tequila Rose Strawberry Cream", "Tequila Rose Strawberry Cream", "Tequila Rose Strawberry Cream",
                    "Tequila Rose Strawberry Cream", "Tequila Rose Strawberry Cream 24Hours Delivery",
                    "Tequila Rose Strawberry Cream 24Hours Delivery", "Terrazas Altos Del Plata Cabernet Sauvignon",
                    "Terrazas Altos Del Plata Chardonnay", "Terrazas Altos Del Plata Malbec",
                    "Terrazas Reserva Cabernet Sauvignon", "Terrazas Reserva Chardonnay", "Terrazas Reserva Malbec",
                    "The Dalmore 12YO", "The Dalmore 15YO", "The Dalmore 18YO", "The Dalmore 25YO",
                    "The Dalmore Cigar Malt Reserve", "The Dalmore King Alexander III", "The Glenlivet 12YO",
                    "The Glenlivet 12YO", "The Glenlivet 15YO", "The Glenlivet 18YO", "The Glenlivet 21YO",
                    "The Glenlivet 25YO", "The Glenlivet Founder's Reserve", "Ultimat", "Ultimat",
                    "Veuve Clicquot Rose Non Vintage", "Veuve Clicquot Rose Vintage 2012",
                    "Veuve Clicquot Yellow Label Non Vintage", "Whisky Glass", "Whisky Glass", "Wine Opener",
                    "Wuliangye 52%", "Wuliangye 52%", "Wuliangye Mellow 50%", "Wuliangye Mellow 50%", "Wyborowa",
                    "Wyndham Bin 222 Chardonnay", "Wyndham Bin 333 Pinot Noir", "Wyndham Bin 444 Cabernet Sauvignon",
                    "Wyndham Bin 555 Shiraz", "Wyndham Bin 888 Cabernet Merlot", "Wyndham Bin 888 Cabernet Merlot",
                    "Wyndham Bin 888 Cabernet Merlot 24Hours Delivery", "Wyndham Bin 999 Merlot",
                    "Wyndham Bin 999 Merlot", "Wyndham Bin 999 Merlot 24Hours Delivery", "Yamazaki 18YO Ltd Edition",
                    "Zhuoneng", "Zhuoneng"]

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

FinalProductNameList_1 = []
FinalProductNameList = []


for productName1 in productNamesList:
    spl_productName = productName1.split(" ")

    try:
        spn_1 = str(spl_productName[0])
        FinalProductNameList_1.append(spn_1)
    except:
        print(productName1)

    try:
        spn_2 = str(spl_productName[0]) + " " + str(spl_productName[1])
        FinalProductNameList_1.append(spn_2)
    except:
        print(productName1)


a1 = set(FinalProductNameList_1)
a1 = list(set(a1))
seen1 = set()
result1 = []
for item1 in a1:
    if item1 not in seen1:
        seen1.add(item1)
        FinalProductNameList.append(item1)

print(FinalProductNameList)
print(len(FinalProductNameList))

print("--------------------------------------------")

print("Web Scrapper Started Successfully ...")
ct = datetime.datetime.now()
print("Start Time :-", ct)

print("--------------------------------------------")


# ------------------------------------------

# All Functions -

#-------------------------------------------------------------------------------------

# Functions for Site 1 - "https://cellarbration.com.sg/" -

def age_verification_1():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="agree-button"]')))
    driver.find_element(By.XPATH, '//button[@class="agree-button"]').click()
    time.sleep(5)


# Function to get all links of products from given website

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
    # time.sleep(2)

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

    # time.sleep(2)

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

# Function to get all links of products from given website

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


# Function to get all links of products from given website

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


# Function to get all links of products from given website

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

# Functions for Site 5 - "https://cellarbration.com.sg/" -

# Function to get all links of products from given website

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


# All Driver Codes -


# -------------------------------------------------------------------------------------

# Driver Code 1 -

driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)

driver.get("https://cellarbration.com.sg/")

print(">> ", driver.title)

age_verification_1()

for productName in FinalProductNameList:

    productName = productName.replace(" ", "%20")

    #Creating Search Links -
    surl = "https://cellarbration.com.sg/catalogsearch/result/index/?product_list_limit=60&q=" + productName

    #Seaching for Products and Collecting Links of Products -
    try:
        driver.get(surl)
        get_links_1()
    except:
        print("No product found for search - ", surl)

# Extracting Uniqque Links -

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

driver.close()

clean_data_1 = [i for n, i in enumerate(finalData_1) if i not in finalData_1[n + 1:]]

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------

# Driver Code 2 -

driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)

driver.get("https://alcohaul.sg/")

print(">> ", driver.title)

age_verification_2()

for productName in FinalProductNameList:

    #Creating Search Links -
    surl = "https://alcohaul.sg/search?search=" + productName

    #Seaching for Products and Collecting Links of Products -
    try:
        driver.get(surl)
        get_links_2()
    except:
        print("No product found for search - ", surl)

# Extracting Uniqque Links -

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

# Collecting Data from Each Link in uniqueLink list -
for lnk2 in uniqueLnks_2:
    get_info_2(lnk2)

    print("Final Data :- ", finalData_2[-1])
    print("No of Product Info. :- ", len(finalData_2))
    print(finalData_2[-1])

driver.close()

clean_data_2 = [i for n, i in enumerate(finalData_2) if i not in finalData_2[n + 1:]]

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------

# Driver Code 3 -

driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)

driver.get("https://www.alcoholporter.com/")

print(">> ", driver.title)

age_verification_3()

for productName in FinalProductNameList:

    #Creating Search Links -
    surl = "https://www.alcoholporter.com/index.php?route=product/search&search=" + productName

    #Seaching for Products and Collecting Links of Products -
    try:
        driver.get(surl)
        get_links_3()
    except:
        print("No product found for search - ", surl)

# Extracting Uniqque Links -

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

# Collecting Data from Each Link in uniqueLink list -
for lnk2 in uniqueLnks_3:
    get_info_3(lnk2)

    print("Final Data :- ", finalData_3[-1])
    print("No of Product Info. :- ", len(finalData_3))
    print(finalData_3[-1])

driver.close()

clean_data_3 = [i for n, i in enumerate(finalData_3) if i not in finalData_3[n + 1:]]

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------

# Driver Code 4 -

driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)

driver.get("https://www.bnb.com.sg/")

print(">> ", driver.title)

age_verification_4()

for productName in FinalProductNameList:

    #Creating Search Links -
    surl = "https://www.bnb.com.sg/index.php?route=product/search&search=" + productName

    #Seaching for Products and Collecting Links of Products -
    try:
        driver.get(surl)
        get_links_4()
    except:
        print("No product found for search - ", surl)

# Extracting Uniqque Links -

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

# Collecting Data from Each Link in uniqueLink list -
for lnk2 in uniqueLnks_4:
    get_info_4(lnk2)

    print("Final Data :- ", finalData_4[-1])
    print("No of Product Info. :- ", len(finalData_4))
    print(finalData_4[-1])

driver.close()

clean_data_4 = [i for n, i in enumerate(finalData_4) if i not in finalData_4[n + 1:]]

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------

# Driver Code 5 -

driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://chuansenghuat.com.sg/")

print(">> ", driver.title)

for productName in FinalProductNameList:

    #Creating Search Links -
    surl = "https://chuansenghuat.com.sg/?s=" + productName + "&post_type=product"

    #Seaching for Products and Collecting Links of Products -
    try:
        driver.get(surl)
        get_links_5()
    except:
        print("No product found for search - ", surl)

# Extracting Uniqque Links -

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

driver.close()

clean_data_5 = [i for n, i in enumerate(finalData_5) if i not in finalData_5[n + 1:]]

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------

# Final Processing -

clean_data = [*clean_data_1, *clean_data_2, *clean_data_3, *clean_data_4, *clean_data_5]
print(clean_data)
print(len(clean_data))

# -------------------------------------------------------------------------------------


# ........................................................................................

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

