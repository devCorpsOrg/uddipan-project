from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
from allLinks import *
import pandas as pd
import pymysql
import openpyxl
import requests
import datetime
import json
import time
import os

# ------------------------------------------

# Global -

finalData_1 = []
finalData_2 = []
finalData_3 = []
finalData_4 = []
finalData_5 = []
finalData_6 = []
finalData_7 = []
finalData_8 = []
finalData_9 = []
finalData_10 = []
finalData_11 = []
finalData_11 = []
finalData_12 = []
finalData_13 = []
finalData_14 = []
finalData_15 = []
finalData_16 = []
finalData_17 = []
finalData_18 = []
finalData_19 = []
finalData_20 = []
finalData_21 = []
finalData_22 = []

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
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


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
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


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
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


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
            price = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/span').text
            price = price.replace("$", "")
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
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


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
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="close-icon"]')))
    driver.find_element(By.XPATH, '//*[@id="close-icon"]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agp_row"]/div/div/div[3]/div/form[1]')))
    driver.find_element(By.XPATH, '//*[@id="agp_row"]/div/div/div[3]/div/form[1]').click()


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
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="comp-k8on02nl"]/a')))
    driver.find_element(By.XPATH, '//*[@id="comp-k8on02nl"]/a').click()


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
            EC.presence_of_element_located((By.XPATH, '//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[2]/div[1]/h1'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[1]/div[2]/section/div/div/pre/p[4]').text
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
        price = driver.find_element(By.XPATH, '//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[2]/div[3]/div/div/div[2]/span[1]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH,'//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[2]/div[3]/div/div/div/span[1]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "gudsht",
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


#-------------------------------------------------------------------------------------

# Functions for Site 20 - "https://cellarbration.com.sg/" -

def age_verification_20():
    pass


def get_info_20(url):
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
            EC.presence_of_element_located((By.XPATH, '//h1[@class="product-title mt-3"]'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volumeObj = driver.find_elements(By.XPATH, '//tr')
        for i in volumeObj:
            if "Bottle volume ml" in i.find_element(By.XPATH, '//td[@class="product__properties__name"]').text:
                volume = i.find_element(By.XPATH, "//td[@class='product__properties__value']").text
                print("volume = ", volume)
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div/span[1]/span').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/nav/div[1]/div/ol/li[3]/a/span').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//span[@class="price price--selling price--discounted"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="price price--selling"]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "paneco",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_20.append(tempV)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------

# Functions for Site 21 - "https://cellarbration.com.sg/" -

def age_verification_21():
    pass

def get_info_21(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume1 = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="product-block product-block--header product-single__header small--hide"]/h1'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="ProductSection-template--14365883957351__main-4585757245543"]/div/div/div[1]/h1').text
            if productName2 == "":
                print("Product Name not found for - ", url)
        except:
            print("Product Name not found for - ", url)

    try:
        time.sleep(4)
        volume = driver.find_elements(By.XPATH, '//div[@class="collapsible-content__inner rte"][1]/p[1]')
        for i in volume:
            print(i)
        volume1 = volume[0].text
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_elements(By.XPATH, '//td[@class="wine_table_columns_second"][1]')
        catagory = catagory[0].text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//span[@class="product__price"]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="price price--selling"]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "primeliquor",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume1,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_21.append(tempV)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------

# Functions for Site 22 - "https://cellarbration.com.sg/" -

def age_verification_22():
    # wait = WebDriverWait(driver, 30)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//md-checkbox[@type="type"]')))
    # time.sleep(5)
    # driver.find_element(By.XPATH, '//select/option[@value="1"]').click()
    # driver.find_element(By.XPATH, '//md-option[@id="select_option_18"]').click()
    # driver.find_element(By.XPATH, '//md-option[@id="select_option_75"]').click()
    # driver.find_element(By.XPATH, '//md-checkbox[@type="type"]').click()
    # driver.find_element(By.XPATH, '///button[@class="ageverify md-button md-ink-ripple"]').click()

    # drop1=Select(driver.find_element(By.XPATH, "//select[@name='userMonth']"))
    # drop1.select_by_value("1")

    # drop2=Select(driver.find_element(By.XPATH, "//select[@name='userDay']"))
    # drop2.select_by_value("1")

    driver.find_element(By.CSS_SELECTOR, '#select_16').click()
    driver.find_element(By.ID, 'select_option_4').click()

    driver.find_element(By.CSS_SELECTOR, '#select_49').click()
    driver.find_element(By.ID, 'select_option_18').click()

    driver.find_element(By.CSS_SELECTOR, '#select_51').click()
    driver.find_element(By.ID, 'select_option_75').click()

    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="ageverify md-button md-ink-ripple"]')))

    time.sleep(5)

    driver.find_element(By.XPATH, '//button[@class="ageverify md-button md-ink-ripple"]').click()

def get_info_22(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        time.sleep(5)
        productName2 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="prddetailtitle ng-binding"]'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="ProductSection-template--14365883957351__main-4585757245543"]/div/div/div[1]/h1').text
            if productName2 == "":
                print("Product Name not found for - ", url)
        except:
            print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1]
    except:
        try:
            volume = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div/div[1]/div/div/div/p[1]/text()[2]').text
        except:
            try:
                volume = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div/div[1]/div/div/div/p[1]/strong[1]').text
            except:
                print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//a[@class="ng-binding ng-scope"]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//div[@class="prddetailpricedicnt ng-binding ng-scope"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="price price--selling"]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "alcoholdelivery",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_22.append(tempV)

#-------------------------------------------------------------------------------------


# All Driver Codes -


# -------------------------------------------------------------------------------------

# Driver Code 1 -

# driver = webdriver.Chrome(ChromeDriverManager().install())  # For IDE (Uncomment in IDE)

site_name = ["https://cellarbration.com.sg/", "https://alcohaul.sg/", "https://www.alcoholporter.com/", "https://www.bnb.com.sg/", "https://chuansenghuat.com.sg/", "https://coldstorage.com.sg/", "https://shop.cornerstonewines.com/", "https://getit.changirecommends.com/", "https://giant.sg/", "https://www.theliquorshop.com.sg/", "https://www.gudsht.org/", "https://www.fairprice.com.sg/", "https://oakandbarrel.com.sg/", "https://www.liquorbar.sg/", "https://thirstydonkey.sg/", "https://www.tyliquor.sg/", "https://www.winesnspirits.sg/", "https://www.oaks.com.sg/", "https://boozemart.sg/","https://www.paneco.com.sg/","https://www.primeliquor.sg/","https://www.alcoholdelivery.com.sg/"]

for sn in site_name:
    driver.get(sn)
    print(">> ", driver.title)

    if sn == "https://cellarbration.com.sg/":
        try:
            age_verification_1()
        except:
            print("Age verification failed")
        for lnk2 in uniqueLnks_1:
            get_info_1(lnk2)
            print("Final Data :- ", finalData_1[-1])
            print("No of Product Info. :- ", len(finalData_1))
            print(finalData_1[-1])
        clean_data_1 = [i for n, i in enumerate(finalData_1) if i not in finalData_1[n + 1:]]
        clean_data_1 = [i for i in clean_data_1 if not (i['Product Name'] == "")]

    elif sn == "https://alcohaul.sg/":
        try:
            age_verification_2()
        except:
            print("Age verification  failed")
        for lnk2 in uniqueLnks_2:
            get_info_2(lnk2)
            print("Final Data :- ", finalData_2[-1])
            print("No of Product Info. :- ", len(finalData_2))
            print(finalData_2[-1])
        clean_data_2 = [i for n, i in enumerate(finalData_2) if i not in finalData_2[n + 1:]]
        clean_data_2 = [i for i in clean_data_2 if not (i['Product Name'] == "")]

    elif sn == "https://www.alcoholporter.com/":
        try:
            age_verification_3()
        except:
            print("Age verification  failed")
        for lnk2 in uniqueLnks_3:
            get_info_3(lnk2)
            print("Final Data :- ", finalData_3[-1])
            print("No of Product Info. :- ", len(finalData_3))
            print(finalData_3[-1])
        clean_data_3 = [i for n, i in enumerate(finalData_3) if i not in finalData_3[n + 1:]]
        clean_data_3 = [i for i in clean_data_3 if not (i['Product Name'] == "")]

    elif sn == "https://www.bnb.com.sg/":
        try:
            age_verification_4()
        except:
            print("Age verification  failed")
        for lnk2 in uniqueLnks_4:
            get_info_4(lnk2)
            print("Final Data :- ", finalData_4[-1])
            print("No of Product Info. :- ", len(finalData_4))
            print(finalData_4[-1])
        clean_data_4 = [i for n, i in enumerate(finalData_4) if i not in finalData_4[n + 1:]]
        clean_data_4 = [i for i in clean_data_4 if not (i['Product Name'] == "")]

    elif sn == "https://chuansenghuat.com.sg/":
        for lnk2 in uniqueLnks_5:
            get_info_5(lnk2)
            print("Final Data :- ", finalData_5[-1])
            print("No of Product Info. :- ", len(finalData_5))
            print(finalData_5[-1])
        clean_data_5 = [i for n, i in enumerate(finalData_5) if i not in finalData_5[n + 1:]]
        clean_data_5 = [i for i in clean_data_5 if not (i['Product Name'] == "")]

    elif sn == "https://coldstorage.com.sg/":
        for lnk2 in uniqueLnks_6:
            r = requests.get(lnk2)
            stat_code = r.status_code
            if stat_code == 200:
                get_info_6(lnk2)
                print("Final Data :- ", finalData_6[-1])
                print("No of Product Info. :- ", len(finalData_6))
                print(finalData_6[-1])
            else:
                time.sleep(30)
        clean_data_6 = [i for n, i in enumerate(finalData_6) if i not in finalData_6[n + 1:]]
        clean_data_6 = [i for i in clean_data_6 if not (i['Product Name'] == "")]

    elif sn == "https://shop.cornerstonewines.com/":
        for lnk2 in uniqueLnks_7:
            get_info_7(lnk2)
            print("Final Data :- ", finalData_7[-1])
            print("No of Product Info. :- ", len(finalData_7))
            print(finalData_7[-1])
        clean_data_7 = [i for n, i in enumerate(finalData_7) if i not in finalData_7[n + 1:]]
        clean_data_7 = [i for i in clean_data_7 if not (i['Product Name'] == "")]

    elif sn == "https://getit.changirecommends.com/":
        for lnk2 in uniqueLnks_8:
            get_info_8(lnk2)
            print("Final Data :- ", finalData_8[-1])
            print("No of Product Info. :- ", len(finalData_8))
            print(finalData_8[-1])
        clean_data_8 = [i for n, i in enumerate(finalData_8) if i not in finalData_8[n + 1:]]
        clean_data_8 = [i for i in clean_data_8 if not (i['Product Name'] == "")]
    elif sn == "https://giant.sg/":
        for lnk2 in uniqueLnks_9:
            get_info_9(lnk2)
            print("Final Data :- ", finalData_9[-1])
            print("No of Product Info. :- ", len(finalData_9))
            print(finalData_9[-1])
        clean_data_9 = [i for n, i in enumerate(finalData_9) if i not in finalData_9[n + 1:]]
        clean_data_9 = [i for i in clean_data_9 if not (i['Product Name'] == "")]

    elif sn == "https://www.theliquorshop.com.sg/":
        for lnk2 in uniqueLnks_10:
            get_info_10(lnk2)
            print("Final Data :- ", finalData_10[-1])
            print("No of Product Info. :- ", len(finalData_10))
            print(finalData_10[-1])
        clean_data_10 = [i for n, i in enumerate(finalData_10) if i not in finalData_10[n + 1:]]
        clean_data_10 = [i for i in clean_data_10 if not (i['Product Name'] == "")]

    elif sn == "https://www.gudsht.org/":
        for lnk2 in uniqueLnks_11:
            get_info_11(lnk2)
            print("Final Data :- ", finalData_11[-1])
            print("No of Product Info. :- ", len(finalData_11))
            print(finalData_11[-1])
        clean_data_11 = [i for n, i in enumerate(finalData_11) if i not in finalData_11[n + 1:]]
        clean_data_11 = [i for i in clean_data_11 if not (i['Product Name'] == "")]

    elif sn == "https://www.fairprice.com.sg/":
        for lnk2 in uniqueLnks_12:
            get_info_12(lnk2)
            print("Final Data :- ", finalData_12[-1])
            print("No of Product Info. :- ", len(finalData_12))
            print(finalData_12[-1])
        clean_data_12 = [i for n, i in enumerate(finalData_12) if i not in finalData_12[n + 1:]]
        clean_data_12 = [i for i in clean_data_12 if not (i['Product Name'] == "")]

    elif sn == "https://oakandbarrel.com.sg/":
        try:
            age_verification_13()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_13:
            get_info_13(lnk2)
            print("Final Data :- ", finalData_13[-1])
            print("No of Product Info. :- ", len(finalData_13))
            print(finalData_13[-1])
        clean_data_13 = [i for n, i in enumerate(finalData_13) if i not in finalData_13[n + 1:]]
        clean_data_13 = [i for i in clean_data_13 if not (i['Product Name'] == "")]

    elif sn == "https://www.liquorbar.sg/":
        for lnk2 in uniqueLnks_14:
            get_info_14(lnk2)
            print("Final Data :- ", finalData_14[-1])
            print("No of Product Info. :- ", len(finalData_14))
            print(finalData_14[-1])
        clean_data_14 = [i for n, i in enumerate(finalData_14) if i not in finalData_14[n + 1:]]
        clean_data_14 = [i for i in clean_data_14 if not (i['Product Name'] == "")]

    elif sn == "https://thirstydonkey.sg/":
        try:
            age_verification_15()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_15:
            get_info_15(lnk2)
            print("Final Data :- ", finalData_15[-1])
            print("No of Product Info. :- ", len(finalData_15))
            print(finalData_15[-1])
        clean_data_15 = [i for n, i in enumerate(finalData_15) if i not in finalData_15[n + 1:]]
        clean_data_15 = [i for i in clean_data_15 if not (i['Product Name'] == "")]

    elif sn == "https://www.tyliquor.sg/":
        try:
            age_verification_16()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_16:
            get_info_16(lnk2)
            print("Final Data :- ", finalData_16[-1])
            print("No of Product Info. :- ", len(finalData_16))
            print(finalData_16[-1])
        clean_data_16 = [i for n, i in enumerate(finalData_16) if i not in finalData_16[n + 1:]]
        clean_data_16 = [i for i in clean_data_16 if not (i['Product Name'] == "")]

    elif sn == "https://www.winesnspirits.sg/":
        try:
            age_verification_17()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_17:
            get_info_17(lnk2)
            print("Final Data :- ", finalData_17[-1])
            print("No of Product Info. :- ", len(finalData_17))
            print(finalData_17[-1])
        clean_data_17 = [i for n, i in enumerate(finalData_17) if i not in finalData_17[n + 1:]]
        clean_data_17 = [i for i in clean_data_17 if not (i['Product Name'] == "")]

    elif sn == "https://www.oaks.com.sg/":
        for lnk2 in uniqueLnks_18:
            get_info_18(lnk2)
            print("Final Data :- ", finalData_18[-1])
            print("No of Product Info. :- ", len(finalData_18))
            print(finalData_18[-1])
        clean_data_18 = [i for n, i in enumerate(finalData_18) if i not in finalData_18[n + 1:]]
        clean_data_18 = [i for i in clean_data_18 if not (i['Product Name'] == "")]

    elif sn == "https://boozemart.sg/":
        try:
            age_verification_19()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_19:
            get_info_19(lnk2)
            print("Final Data :- ", finalData_19[-1])
            print("No of Product Info. :- ", len(finalData_19))
            print(finalData_19[-1])
        clean_data_19 = [i for n, i in enumerate(finalData_19) if i not in finalData_19[n + 1:]]
        clean_data_19 = [i for i in clean_data_19 if not (i['Product Name'] == "")]

    elif sn == "https://www.paneco.com.sg/":
        try:
            age_verification_20()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_20:
            get_info_20(lnk2)
            print("Final Data :- ", finalData_20[-1])
            print("No of Product Info. :- ", len(finalData_20))
            print(finalData_20[-1])
        clean_data_20 = [i for n, i in enumerate(finalData_20) if i not in finalData_20[n + 1:]]
        clean_data_20 = [i for i in clean_data_20 if not (i['Product Name'] == "")]

    elif sn == "https://www.primeliquor.sg/":
        try:
            age_verification_22()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_21:
            get_info_21(lnk2)
            print("Final Data :- ", finalData_21[-1])
            print("No of Product Info. :- ", len(finalData_21))
            print(finalData_21[-1])
        clean_data_21 = [i for n, i in enumerate(finalData_21) if i not in finalData_21[n + 1:]]
        clean_data_21 = [i for i in clean_data_21 if not (i['Product Name'] == "")]

    elif sn == "https://www.alcoholdelivery.com.sg/":
        try:
            age_verification_22()
        except Exception as e:
            print("Age verification failed !", e)
        for lnk2 in uniqueLnks_22:
            get_info_22(lnk2)
            print("Final Data :- ", finalData_22[-1])
            print("No of Product Info. :- ", len(finalData_22))
            print(finalData_22[-1])
        clean_data_22 = [i for n, i in enumerate(finalData_22) if i not in finalData_22[n + 1:]]
        clean_data_22 = [i for i in clean_data_22 if not (i['Product Name'] == "")]
    else:
        driver.close()

driver.close()

# Final Processing -

clean_data = [*clean_data_1, *clean_data_2, *clean_data_3, *clean_data_4, *clean_data_5, *clean_data_6, *clean_data_7, *clean_data_8, *clean_data_9, *clean_data_10, *clean_data_11, *clean_data_12, *clean_data_13, *clean_data_14, *clean_data_15, *clean_data_16, *clean_data_17, *clean_data_18, *clean_data_19, *clean_data_20, *clean_data_21, *clean_data_22]
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
    engine = create_engine("mysql+pymysql://dev:devAverps3985$$@128.199.122.126/uddipan?charset=utf8mb4")
    df = pd.read_json("finalData.json")
    df.to_sql("Product_prices", con=engine, if_exists="replace", index=False)
    print("Data updated in Database...")
except:
    print(">> Cannot Connect to Database")

# ........................................................................................


print("--------------------------------------------")

logFile = open("scrapperLogs.txt", "a")

ct1 = datetime.datetime.now()

print("Start Time :-", ct)
print("End Time :-", ct1)

ct = str(ct)
ct1 = str(ct1)
logFile.write("Start Time = ", ct)
logFile.write(str("Stop Time = " + ct1))

logFile.close()

print("--------------------------------------------")



"Barton","Larios","Pinnacle","Rain Organics Original","Rain Organics Red Grape Hibiscus","Rain Organics Lavender Lemonade","Rain Organics Cucumber Lime","Wyborowa","Absolut Original","Absolut Citron","Absolut Kurant","Absolut Vanilia","Absolut Apeach","Absolut Vanilia","Royal Dragon Superior","Absolut Elyx Flare","Ciroc","Ketel One Original","Ketel One Citroen","Smirnoff No.21","Smirnoff Black","Belvedere Pure","Belvedere Pink Grapefruit","Diesel 190 Proof","Gordon's","Gordon's Pink","Broker's","Beefeater","Beefeater 24","Monkey 47 Dry","Monkey 47 Sloe","Gilbey's","Tanqueray","Tanqueray Rangpur","Tanqueray Sevilla","Tanqueray Ten","Jim Beam White","Bulleit Frontier","Bulleit Rye","Montezuma Gold","Montezuma Silver","Sauza Extra Gold","Jose Cuervo","Olmeca Reposado","El Recuerdo de Oaxaca","Altos Plata","Altos Reposado","Casamigos Anejo","Casamigos Blanco","Casamigos Joven","Casamigos Reposado","Don Julio 1942","Don Julio Blanco","Don Julio Reposado","Don Julio Anejo","Nikka From the Barrel","Highland Mist","Mackinlay's Shackleton","Teacher's Origin","Chivas Regal 12YO","Chivas Regal XV Gold 15YO","Chivas Regal Extra","Chivas Regal Mizunara","Chivas Regal 25YO","Royal Salute 21YO","Royal Salute 62 Gun","Ballantine's Finest","Ballantine's 17YO","Ballantine's 21YO","Ballantine's 30YO","John Jameson","Black & White","J&B Rare","Johnnie Walker Red Label","Johnnie Walker Ltd Edition White Walker","Johnnie Walker Black Label","Johnnie Walker Double Black","Johnnie Walker Gold Label Reserve","Johnnie Walker Green Label 15YO","Johnnie Walker 18YO","Johnnie Walker Blue Label","Johnnie Walker XR21","Naked Grouse","Ardmore","Copper Dog","Bowmore 12YO","Bowmore 18YO","Bowmore 25YO","Hakushu Distiller's Reserve","Glenrothes Vintage 1985","Jura 12YO","Jura 18YO","Jura Seven Wood","The Dalmore 12YO","The Dalmore 15YO","The Dalmore 18YO","The Dalmore Cigar Malt Reserve","The Dalmore King Alexander III","The Dalmore 25YO","The Glenlivet Founder's Reserve","The Glenlivet 12YO Double Oak","The Glenlivet 15YO French Oak Reserve","The Glenlivet 18YO","The Glenlivet 21YO","The Glenlivet 25YO","Aberlour 12YO Double Cask","Aberlour 16YO Double Cask","Aberlour 18YO","Caol ILA 12YO","Cardhu 12YO","Clynelish 14YO","Cragganmore 12YO","Dalwhinnie 15YO","Glenkinchie 12YO","Lagavulin 16YO","Oban 14YO","Mortlach 12YO","Mortlach 16YO","Mortlach 20YO","Royal Lochnagar 12YO","Singleton Dufftown 12YO","Singleton Dufftown 15YO","Singleton Dufftown 18YO","Talisker 10YO","Talisker 18YO","Glenfarclas 12YO","Glenfarclas 15YO","Glenfarclas 17YO","Glenfarclas 21YO","Glenfarclas 25YO","Glenfarclas 30YO","Glenfarclas 40YO","Nikka Taketsuru","Nikka Taketsuru 17YO","Nikka Taketsuru 21YO","Glenmorangie 10YO Original","Glenmorangie 18YO Extremely Rare","Glenmorangie 12YO The Lasanta","Glenmorangie 14YO Quinta Ruban","Glenmorangie Nectar d'Or Rare Cask","Glenmorangie Signet","Ardbeg 10YO","Martell VSOP","Martell VSOP","Martell VSOP","Martell Cordon Bleu","Martell Cordon Bleu","Martell Cordon Bleu","Martell Cordon Bleu","Martell Cordon Bleu","Martell XO","Martell NCF","Hennessy VSOP","Hennessy XO","Hennessy Paradis","Hennessy Richard","Saratoga Dark","Havana Club 3YO","Havana Club 7YO","Captain Morgan White","Captain Morgan Spiced Gold","Captain Morgan Dark","Ron Zacapa Sistema Solera Centenario 23","Ron Zacapa Solera Centenario XO","Tequila Rose Strawberry Cream","Tequila Rose Strawberry Cream","Tarantula Azul","Montezuma Triple Sec","di Amore Quattro Orange","Malibu Coconut Rum","Kahlua Coffee","Baileys Cream","Archers Peach Schnapps","Pimm's Aperitif","Absolut Original","Absolut Original","Smirnoff Red","Smirnoff Red","Gordon's","Gordon's","Black Velvet","Johnnie Walker Red Label","Johnnie Walker Red Label","Johnnie Walker Black Label","Chivas Regal 12YO","Chivas Regal 12YO","Martell VSOP","Black & White","Absolut Original","Barton","McCormick Apple","Fleischmann's Vanilla","Rain Organics Cucumber Lime","Gordon's","Johnnie Walker Red Label","Johnnie Walker Black Label","Chivas Regal 12YO","Chivas Regal 18YO","The Glenlivet 12YO","Monte Alban","Patron Anejo","Patron Reposado","Patron Silver","Montezuma Silver","Montezuma Gold","Bacardi Superior","di Amore Sambucca","di Amore Amaretto","Tarantula Azul","Schnapps 99 Apple","Schnapps 99 Bananas","Schnapps 99 Blackberries","Schnapps 99 Orange","Patron XO Cafe","Patron XO Cafe Dark Cocoa","Paulaner Munich Hell Lager","Paulaner Munich Hell Lager","Paulaner Weissbier Wheat","Paulaner Weissbier Dunkel Dark Wheat","Malesan Rouge VDT 2020","Malesan Blanc VDT 2021","Malesan Rouge Bordeaux Terra Vitis AOC 2019","Malesan Medoc AOC 2019","Maison Louis Girard Pinot Noir Burgundy AOC 2020","Maison Louis Girard Coteaux Burgundy AOC 2019","Chateau Coutet Grand Vin de Sauternes 2017","Chateau Coutet Grand Vin de Sauternes 2018","Chateau Clos Floridene Grand Vin de Graves 2018","Chateau Latour Carnet Haut-Medoc AOC 2016","Chateau Fonreaud Listrac-Medoc AOC 2011","Alter Ego De Palmer Margaux AOC 2013","Chateau Cantenac Brown Margaux AOC 2018","Chateau Du Tertre Margaux Grand Cru 2018","Dame De Bouard Montagne-St-Emilion AOC 2018","Chateau D'Armailhac Pauillac AOC 2017","Chateau Pichon Baron Pauillac Grand Cru 2014","Fugue De Nenin Pomerol AOC 2018","Chateau Chauvin St-Emilion Grand Cru 2016","Chateau Pedesclaux Pauillac Grand Cru 2017","Chateau Lafon Rochet St-Estephe AOC 2011","Cape Mentelle Sauvignon Blanc Semillon 2019","Cape Mentelle Chardonnay 2018","Cape Mentelle Cabernet Merlot 2016","Cape Mentelle Shiraz 2017","Jacob's Creek Shiraz Cabernet 2020","Jacob's Creek Cabernet Sauvignon 2020","Jacob's Creek Grenache Shiraz 2020","Jacob's Creek Merlot 2020","Jacob's Creek Shiraz 2020","Jacob's Creek Chardonnay 2020","Jacob's Creek Riesling 2020","Jacob's Creek Sauvignon Blanc 2020","Jacob's Creek Chardonnay","Jacob's Creek Shiraz Cabernet","Jacob's Creek Twin Pickings Pinot Gris 2019","Jacob's Creek Twin Pickings Sauvignon Blanc 2019","Jacob's Creek Reserve Shiraz 2018","Jacob's Creek Reserve Cabernet Sauvignon 2018","Jacob's Creek Reserve Chardonnay 2019","Jacob's Creek Reserve Riesling 2018","Jacob's Creek Double Barrel Shiraz 2018","Jacob's Creek Double Barrel Cabernet Sauvignon 2018","St Hugo Shiraz","St Hugo Cabernet Sauvignon","Wyndham Bin 222 Chardonnay 2020","Wyndham Bin 333 Pinot Noir 2019","Wyndham Bin 444 Cabernet Sauvignon 2019","Wyndham Bin 555 Shiraz 2020","Wyndham Bin 888 Cabernet Merlot 2019","Wyndham Bin 999 Merlot 2019","Brancott Estate Marlborough Sauvignon Blanc 2020","Brancott Estate Pinot Noir 2018","Brancott Estate Letter 'B' Sauvignon Blanc 2017","Brancott Estate Letter 'T' Pinot Noir 2017","Cloudy Bay Sauvignon Blanc 2021","Cloudy Bay Chardonnay 2020","Cloudy Bay Te Koko 2017","Cloudy Bay Pinot Noir 2019","Campo Viejo Tempranillo 2018","Campo Viejo Viura 2018","Graffigna Pinot Grigio Reserve","Terrazas Altos Del Plata Chardonnay 2018","Terrazas Altos Del Plata Cabernet Sauvignon 2019","Terrazas Altos Del Plata Malbec 2019","Terrazas Reserva Chardonnay 2020","Terrazas Reserva Cabernet Sauvignon 2019","Terrazas Reserva Malbec 2019","Jacob's Creek Chardonnay Pinot Noir","Jacob's Creek Rose","Jacob's Creek Dots Moscato Rose","Cafe De Paris","Cafe De Paris Lychee","Cafe De Paris Peach","Chandon Brut Non Vintage","Chandon Rose Non Vintage","Mumm Cordon Rouge Non Vintage","Mumm Rose Non Vintage","Perrier Jouet Grand Brut Non Vintage","Perrier Jouet Belle Epoque Vintage 2013","Perrier Jouet Belle Epoque Rose Vintage 2012","Perrier Jouet Blason Rose Non Vintage","Moet & Chandon Imperial Non Vintage","Moet & Chandon Imperial Rose Non Vintage","Veuve Clicquot Yellow Label Non Vintage","Veuve Clicquot Rose Non Vintage","Veuve Clicquot Rose Vintage 2012","Krug Grande Cuvee 169 Edition Non Vintage","Krug Vintage 2006","Ruinart Blanc de Blancs Non Vintage","Ruinart Rose Non Vintage","Matsui San-In","Matsui Kurayoshi 12YO","Matsui Kurayoshi 25YO","Matsui Kurayoshi 33YO","Matsui Kurayoshi 8YO","Matsui Kurayoshi","Matsui Kurayoshi Sherry Cask","Matsui Mizunara Cask","Matsui The Peated","Matsui Sakura","Matsui Tottori 17YO","Matsui Tottori 21YO","Matsui Tottori 23YO","Matsui Tottori 27YO","Matsui Tottori","Matsui Umeshu Brandy","Matsui Umeshu Whisky","Nikka Coffey","Nikka Coffey","Nikka Super Rare Old","Penfolds Bin 128 Shiraz 2019","Penfolds Bin 2 Shiraz Mataro 2019","Penfolds Bin 28 Shiraz 2019","Penfolds Bin 407 Cabernet Sauvignon 2019","Penfolds Bin 8 Shiraz Cabernet 2019","Penfolds Grange Bin 95 Shiraz 2013","Jinro Flavour 10xGrapefruit 10xStrawberry","Jinro Flavour 10xPlum 10xGrapefruit","Jinro Flavour 10xStrawberry 10xPlum","Jinro Chamisul Fresh","Jinro Grapefruit","Jinro Plum","Jinro Strawberry","Carlsberg Danish Pilsner","Asahi Super Dry","Asahi Super Dry Black","Paulaner Oktoberfest","Kronenbourg 1664 Blanc","Kronenbourg 1664 Lager","Corona Extra","Auchentoshan 12YO Triple Distilled","Balvenie 40YO","Yamazaki 18YO Limited Edition","Courvoisier Premier Reserve","Courvoisier Napoleon","Courvoisier XO","Hennessy Prive","Martell Chanteloup XXO","Martell Cordon Bleu Prestige Ltd Edition","Patron Anejo","Patron Citronge Orange","Patron Reposado","Patron Roca Anejo","Patron Roca Reposado","Patron Silver Bee Ltd Edition","Patron Silver","Patron XO Café","Ruinart R De Non Vintage","Ardbeg Corryvreckan","Ardbeg Uigeadail","Black & White","Chivas Regal 18YO","Pernod","Smirnoff Red","Absolut Original","Absolut Vanilia","Auchentoshan 12YO Triple Distilled","Black Velvet","Chandon Brut Non Vintage","Chivas Regal 18YO","Highland Mist","Jagermeister","Johnnie Walker Black Label","Johnnie Walker Red Label","Johnnie Walker White Walker","Jose Cuervo","Malesan Blanc VDT 2021","Malesan Rouge VDT 2020","Mumm Cordon Rouge Non Vintage","Singleton Dufftown 12YO","Singleton Dufftown 15YO","Singleton Dufftown 18YO","Teacher's Origin","Tequila Rose Strawberry Cream","Tequila Rose Strawberry Cream","Naked Grouse","Wyndham Bin 888 Cabernet Merlot 2019","Wyndham Bin 999 Merlot 2019","Wyndham Bin 999 Merlot 2019","Wyndham Bin 888 Cabernet Merlot 2019","Absolut Original","Absolut Vanilia","Chivas Regal 12YO & 18YO","Diesel 190 Proof","Glenfarclas 15YO","Glenfarclas 17YO","Singleton Dufftown 12YO","Bottega Stardust Prosecco DOC","Hibiki 21YO Mount Fuji Ltd Edition","Alexander Society Flute Glass","Golden Glass","Crystal Head Skull Stem Martini Glass","Jack Daniel’s Honey","Absolut Mandrin","Bottega 0 Rose","Bottega Fragolino Rosso Party","Bottega Rose Gold","Bottega Gold Prosecco","Bottega Rose Brut DOC","Bottega Petalo Amore","Bottega Stardust No Liquid","Bottega Stardust No Liquid","Crystal Head","Crystal Head Original Bottle No Liquid","Cutty Sark","Don Julio Reposado","Dom Perignon Rose Vintage 2006","Dom Perignon Vintage 2010","Hennessy XO","Hibiki 17YO","Hine XO","Jack Daniel’s Old No. 7","Maker's Mark","Somersby Cider Sparkling Rose","Somersby Cider Pear","Somersby Cider Apple","Jinro Flavour 1xGrapefruit 1xPlum 2x Strawberry","Jinro Flavour 3xGrapefruit 3xPlum 2xStrawberry","Jinro Flavour 3xGrapefruit 3xPlum 4xStrawberry","Baileys Cream","Jim Beam White","Montezuma Gold","Montezuma Silver","Patron XO Café Dark Cocoa","Cloudy Bay Sauvignon Blanc 2021","Malesan Rouge VDT 2020","Malesan Blanc VDT 2021","Singleton Dufftown 12YO","Glen Grant 10YO","Glen Grant 12YO","Glen Grant 15YO","Glen Grant 18YO","Bottega Poeti Prosecco","Sauza Extra Gold","Singleton Dufftown 12YO & 15YO","Tequila Rose Strawberry Cream","Tequila Rose Strawberry Cream","Nikka From the Barrel","Chivas Regal 12YO & 18YO","Chivas Regal 12YO","Bottega Poeti Prosecco 2021","Bottega Soave Classico DOC 2017","Jacob's Creek Dots Moscato White","Matsui Tottori Bourbon Barrel","Johnnie Walker Red Label","Ballantine's 12YO","Bottega Petalo Amore","Crystal Head","Rain Organics Original","Ultimat","di Amore Raspberry","Ricard","Ultimat","Rain Organics Red Grape Hibiscus","Bowmore 12YO & 18YO","Matsui Kurayoshi 18YO ","John Jameson","Martell Noblige",
',"","Wuliangye 52%","Montezuma Gold","Montezuma Silver","Wuliangye Mellow 50%","Wuliangye 52%","Wuliangye Mellow 50%","Chivas Regal Extra 13YO American Rye","Chivas Regal Extra 13YO Sherry Cask","Absolut Extrakt","Mumm Blanc de Blancs Non Vintage","Chivas Regal Extra 13YO American Rye & Sherry Cask","Rail Mat","Patron Rail Mat","Patron Condiments Tray","Patron Cocktail Shaker","Patron Napkin Holder","Cutting Board","Hennessy VSOP","Passport","El Recuerdo de Oaxaca","McCormick Orange","McCormick Raspberry","McCormick Vanilla","Jose Cuervo Shot Glass","Patron Shot Glass","Rocks Glass","Chivas Regal XV Gold 15YO","Moet & Chandon Imperial Non Vintage","Moet & Chandon Imperial Non Vintage","Wine Bucket","Ice Bucket","Patron Ice Bucket","Wine Opener","Gordon's","Gordon's","Smirnoff Red","Smirnoff Red","Martell VSOP","Jacob's Creek Chardonnay","Jacob's Creek Shiraz Cabernet 2020","Johnnie Walker Red Label","Johnnie Walker Red Label","Johnnie Walker Black Label","Chateau Coutet Grand Vin de Sauternes 2017","Chateau Coutet Grand Vin de Sauternes 2018","Chateau Clos Floridene Grand Vin de Graves 2018","Chateau Latour Carnet Haut-Medoc AOC 2016","Chateau Fonreaud Listrac-Medoc AOC 2011","Chateau Cantenac Brown Margaux AOC 2018","Chateau Du Tertre Margaux Grand Cru 2018","Dame De Bouard Montagne-St-Emilion AOC 2018","Chateau D'Armailhac Pauillac AOC 2017","Chateau Pichon Baron Pauillac Grand Cru 2014","Fugue De Nenin Pomerol AOC 2018","Chateau Chauvin St-Emilion Grand Cru 2016","Chateau Pedesclaux Pauillac Grand Cru 2017","Chateau Lafon Rochet St-Estephe AOC 2011","Alter Ego De Palmer Margaux AOC 2013","Malesan Blanc VDT 2021","Malesan Rouge VDT 2020","Luminarc Shot Glass","Penfolds Bin 389 Cabernet Shiraz 2019","Penfolds Bin 2 Shiraz Mataro 2019","Penfolds Bin 389 Cabernet Shiraz 2019","Penfolds Bin 8 Shiraz Cabernet 2019","Penfolds Bin 128 Shiraz 2019","Dewar's 15YO","Dewar's White Label","Baron Otard VSOP","Dewar's 12YO","Baron Otard VSOP","Baron Otard VSOP","Grey Goose","Benedictine DOM","Bacardi Carta Blanca","Bacardi Carta Oro Gold","Bacardi Carta Negra","Bacardi Oak Heart","Camino Silver","Campari","Camino Gold","Aberfeldy 12YO","Aperol","Martini Asti Spumante","Bulldog","Martini Rosso Vermouth","Skyy","Martini Extra Dry Vermouth","Martini Bianco Vermouth","Wild Turkey","American Honey","Martini Prosecco","Grand Marnier Cordon Rouge","Monkey Shoulder","Martini Brut","Martini Rose","Balvenie 12YO Triple Cask","Glen Deveron 16YO","Glen Deveron 20YO","19 Crimes Shiraz","19 Crimes Cabernet Sauvignon","Matua Marlborough Pinot Noir","Matua Marlborough Sauvignon Blanc","Lindemans Bin 25 Chardonnay","Lindemans Bin 40 Merlot 2019","Lindemans Bin 45 Cabernet Sauvignon 2020","Lindemans Bin 50 Shiraz 2020","Lindemans Bin 65 Chardonnay 2020","Lindemans Bin 95 Sauvignon Blanc","Lindemans Bin 99 Pinot Noir 2018","Rawson's Retreat Merlot 2019","Rawson's Retreat Cabernet Sauvignon 2019","Rawson's Retreat Private Release Shiraz Cabernet 2019","Rawson's Retreat Shiraz Cabernet 2019","Rawson's Retreat Chardonnay 2019","Rawson's Retreat Semillon Sauvignon Blanc","Remy Martin Cellar No 16","Bacardi Mango Fusion","Bacardi Limon","Bombay Sapphire","Rosemount Meal Matcher Shiraz","Rawson's Retreat Semillon Sauvignon Blanc","Rawson's Retreat Chardonnay 2019","Rawson's Retreat Shiraz Cabernet 2019","Lindemans Bin 99 Pinot Noir 2020","Rawson's Retreat Merlot 2019","Lindemans Bin 95 Sauvignon Blanc","Lindemans Bin 65 Chardonnay 2020","Lindemans Bin 50 Shiraz 2021","Lindemans Bin 45 Cabernet Sauvignon 2021","Lindemans Bin 40 Merlot 2019","Lindemans Bin 25 Chardonnay","Rawson's Retreat Private Release Shiraz Cabernet 2019","Rawson's Retreat Cabernet Sauvignon 2020","Patron XO Cafe Dark Cocoa","Patron XO Cafe","Patron Silver","Patron Reposado","Patron Anejo","Davidoff XO","Davidoff VSOP","Bacardi Ocho 8YO","Dewar's 18YO","Black & White","Chivas Regal 18YO","Singleton Dufftown 12YO","Davidoff VS","Aberlour 12YO Double Cask","Remy Martin XO","Label 5 Classic Black","Skyy Berry","Midori Melon","Skyy 90","Vaccari Sambuca","Terra Dourada Ouro Cachaca","Terra Dourada Cachaca","Terra Dourada Caipirinha Cachaca","Sea Wynde","Evan Williams 7YO","Smirnoff Citrus Twist","Smirnoff Vanilla Twist","Smirnoff Orange Twist","Smirnoff Raspberry Twist","Smirnoff No.21","Smirnoff No.57","Ketel One","Beluga Noble Russian","42 Below Passionfruit","Belvedere","Stolichnaya","Maker's Mark","Skyy","Skyy Vanilla","Sir Edward's Finest","Woodford Reserve Distiller's Select","Famous Grouse Finest","Polignac VSOP","Polignac VS","Polignac Premier Grand Cru","Grand Marnier","Bundaberg","Courvoisier XO","Courvoisier Exclusif","Absolut Level","Royal Salute 21YO","The Glenlivet 15YO French Oak Reserve","Mumm Cordon Rouge Non Vintage","Mumm Cordon Rouge Non Vintage","The Glenlivet Founder's Reserve, 12YO & 15YO","The Glenlivet Founder's Reserve & 15YO","Paulaner Weissbier Alcohol Free","1800 Reserva Reposado","LeMercier Absinthe","Bacardi Gold","Bacardi Limon","Bombay Sapphire","Canadian Club","Canadian Mist","Chivas Regal 12YO","Chopin","Drambuie","Gentleman Jack","Glenmorangie 10YO","Gordon's Deluxe","Hennessy Bras D'or","Jose Cuervo Black Medallion","Jose Cuervo Gold","MacArthur's Select","Malibu Coconut Rum","Martell Cordon Bleu","Martell VSOP","Montego Bay Gold","Baron Otard XO","Remy Martin VSOP","Romana Sambuca","Tanqueray","Teacher's Highland Cream","The Balvenie 10YO Founder's Reserve","Wild Turkey 101","Ballantine's Finest","Campari","Dewar's White Label","Grey Goose","Martini Extra Dry Vermouth","Martini Rosso Vermouth","Saratoga Dark","Bacardi Superior","Cutty Sark","Tequila Rose","Tequila Rose Strawberry Cream","Janneau VSOP","Level 33 Brut Craft","Bottega Ipanema Cachaca","Martell Cordon Bleu","The Glenlivet 12YO Double Oak","The Glenlivet Founder's Reserve & 12YO Double Oak","Martell Cordon Bleu","Ballantine's 21YO","Ballantine's Finest","Aberlour 16YO Double Cask","The Glenlivet Founder's Reserve","The Glenlivet 15YO French Oak Reserve","Gordon's Pink","Paulaner Oktoberfest","Paulaner Weissbier Dunkel Dark Wheat","Paulaner Weissbier Wheat","Macallan Lumina","J&B Rare","Mumm Cordon Rouge Non Vintage","Perrier Jouet Grand Brut Non Vintage","Perrier Jouet Grand Brut Non Vintage","Perrier Jouet Grand Brut Non Vintage","Perrier Jouet Grand Brut Non Vintage","Royal Salute 38YO","Ballantine's 21YO","Aberlour 18YO","The Glenlivet 18YO","The Glenlivet 18YO","Penfolds Bin 28 Shiraz 2019","Penfolds Koonunga Hill Cabernet Sauvignon 2019","Penfolds Koonunga Hill Cabernet Sauvignon 2019","Penfolds Koonunga Hill Shiraz Cabernet 2019","Penfolds Koonunga Hill Shiraz Cabernet 2019","Penfolds Koonunga Hill Shiraz 2020","Penfolds Koonunga Hill Shiraz 2020","Penfolds St. Henri Shiraz 2017","Penfolds St. Henri Shiraz 2017","Chivas Regal 12YO","Chivas Regal 12YO","Paulaner Weissbier Alcohol Free","Chivas Regal 12YO","Chivas Regal 18YO","Martell L'Or de Jean Martell","Corona Extra","Corona Extra","Somersby Cider Sparkling Rose","Somersby Cider Apple","Somersby Cider Pear","Kronenbourg 1664 Blanc","Kronenbourg 1664 Lager","Hakushu 18YO Limited Edition","Araid 18YO Limited Edition","Penfolds Max Shiraz 2019","Penfolds Max Shiraz 2019","Royal Salute 21YO","Martell Noblige",
',"","Martell VSOP","Martell Cordon Bleu","Paulaner Munich Hell Lager","The Glenlivet Founder's Res, 12YO, 15YO & 18YO","Wyndham Bin 333 Pinot Noir 2019","Wyndham Bin 555 Shiraz 2020","Paulaner Munich Hell Lager","Caperdonich 30YO","Broker's","Absolut Original","Absolut Original","Martell Noblige",
',"","Johnnie Walker Red Label","Corona Extra","Baileys Cream","Ballantine's Finest","Penfolds Max Shiraz 2019","Penfolds St. Henri Shiraz 2017","Penfolds Koonunga Hill Shiraz 2020","Penfolds Koonunga Hill Shiraz Cabernet 2019","Penfolds Koonunga Hill Cabernet Sauvignon 2019","Penfolds Bin 28 Shiraz 2019","Penfolds Bin 2 Shiraz Mataro 2019","Penfolds Bin 128 Shiraz 2019","Penfolds Bin 8 Shiraz Cabernet 2019","Chivas Regal Mizunara","Hoegaarden Wheat","Hoegaarden Wheat","Balvenie 16YO Triple Cask","Balvenie 16YO Triple Cask","Balvenie 12YO Triple Cask","Chivas Regal Mizunara","Martell VSOP","Martell VSOP","Chivas Regal 12YO","Wyndham Bin 222 Chardonnay 2019","Wyndham Bin 444 Cabernet Sauvignon 2019","Jacob's Creek Shiraz Cabernet 2020","Jacob's Creek Shiraz Cabernet 2020","Jacob's Creek Chardonnay 2020","Jacob's Creek Chardonnay 2020","Jacob's Creek Cabernet Sauvignon 2020","Corona Extra","Corona Extra","Martell Cordon Bleu","Perrier Jouet Blanc De Blanc Non Vintage","Tanqueray Sevilla","Penfolds Max Cabernet Sauvignon 2019","Penfolds Max Cabernet Sauvignon 2019","Penfolds Max Cabernet Sauvignon 2019","Penfolds Max Shiraz Cabernet 2020","Penfolds Max Shiraz Cabernet 2020","Penfolds Max Shiraz Cabernet 2020","Penfolds Bin 389 Cabernet Shiraz 2019","Penfolds Bin 707 Cabernet Sauvignon 2019","Penfolds Bin 707 Cabernet Sauvignon 2019","Penfolds Grange Bin 95 Shiraz 2017","Jinro Green Grape","Budweiser","Budweiser","Wolf Blass Red Label Shiraz Cabernet 2021","Wolf Blass Gold Label Regional Reserve Cabernet Sauvignon 2019","Wolf Blass Gold Label Regional Reserve Shiraz 2016","Wolf Blass Grey Label McLaren Vale Shiraz 2017","Wolf Blass Black Label Cabernet Shiraz Malbec 2018","Wolf Blass Red Label Shiraz Cabernet 2021","Wolf Blass Red Label Shiraz Cabernet 2021","Wolf Blass Gold Label Regional Reserve Cabernet Sauvignon 2019","Wolf Blass Gold Label Regional Reserve Cabernet Sauvignon 2019","Wolf Blass Gold Label Regional Reserve Shiraz 2016","Wolf Blass Gold Label Regional Reserve Shiraz 2016","Wolf Blass Grey Label McLaren Vale Shiraz 2017","Wolf Blass Grey Label McLaren Vale Shiraz 2017","Wolf Blass Black Label Cabernet Shiraz 2018","Wolf Blass Black Label Cabernet Shiraz Malbec 2018","Remy Martin XO","Chateau Mauvesin Barton Moulis-en-Médoc AOC 2011","Chateau Mauvesin Barton Moulis-en-Médoc AOC 2011","Reserve De La Comtesse Pauillac AOC 2011","Reserve De La Comtesse Pauillac AOC 2011","Chateau Carbonnieux Pessac-Leognan AOC 2011","Chateau Carbonnieux Pessac-Leognan AOC 2011","Chateau Pontac Monplaisir Pessac-Leognan AOC 2011","Chateau Pontac Monplaisir Pessac-Leognan AOC 2011","Chateau Faugeres Saint-Emilion Grand Cru 2011","Chateau Faugeres Saint-Emilion Grand Cru 2011","Chateau St Pierre Saint-Julien AOC 2011","Chateau St Pierre Saint-Julien AOC 2011","Chateau Chauvin St-Emilion Grand Cru 2011","Chateau Chauvin St-Emilion Grand Cru 2011","Chateau Lafon Rochet St-Estephe AOC 2012","Chateau Lafon Rochet St-Estephe AOC 2012","Macallan 25YO Sherry Oak","Macallan 30YO Sherry Oak","Macallan 1824 Oscuro","Macallan Rare Cask Black","Macallan Quest","Macallan Concept Number 3","Macallan The Harmony Collection","Balvenie 25YO","Auchentoshan 18YO Triple Distilled","Courvoisier VSOP","Remy Martin Louis XIII","Ace of Spades Armand de Brignac Brut Non Vintage","Bottega Poeti Prosecco Extra Dry 2021","Bottega White Gold","Bottega Pink Manzoni Moscato","Bottega Stella Blue Millesimato","Bottega Stella Rosa Millesimato","Bottega Millesimato","Bottega Gold Prosecco","Bottega Rose Gold","Bottega Trevenezie Cabernet Sauvignon IGT 2021","Bottega Trevenezie Merlot IGT 2021","Bottega Venezia Pinot Grigio DOC 2021","Bottega Delle Venezie Pinot Grigio Rose 2021","Bottega Acino D'Oro Chianti DOCG 2020","Bottega Acino D'Oro Chianti Classico Riserva DOCG 2015","Bottega Amarone Della Valpolicella DOCG 2017","Davidoff XXO","Ballantine's Finest","Ballantine's Finest","Ballantine's Finest","Ballantine's Finest","Ballantine's 12YO","Chivas Regal 18YO","Absolut Grapefruit","Chivas Regal Extra 13YO Tequila Cask","Chivas Regal Extra 13YO Bourbon Cask","Sauza Extra Silver","Vaccari Sambuca","Davidoff VSOP","Bottega Gold Prosecco","Bottega Pink Manzoni Moscato","Jacob's Creek Dots Moscato White","Jacob's Creek Dots Moscato Rose","Jacob's Creek Chardonnay Pinot Noir","Jacob's Creek Rose","Jacob's Creek Riesling 2020","Jacob's Creek Shiraz Cabernet 2019","Jacob's Creek Shiraz 2019","Jacob's Creek Merlot 2020","Jacob's Creek Cabernet Sauvignon 2020","Johnnie Walker Black Label","Penfolds Bin 407 Cabernet Sauvignon 2019","Johnnie Walker Red Label"


