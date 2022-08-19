#from attr import field
from flask import Flask, request
import flask
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json
import atexit
import werkzeug.exceptions
import requests
from loguru import logger
from config import config
from tools import *
from log import *
import db
import os

from CreateDataBase import create

db = db.db

app = Flask(__name__)

# log = log.log()
app.config['MYSQL_HOST'] = config['MYSQL_HOST']
app.config['MYSQL_USER'] = config['MYSQL_USER']  # username
app.config['MYSQL_PASSWORD'] = config['MYSQL_PASSWORD']  # password
app.config['MYSQL_DB'] = config['MYSQL_DB']  # database name

# Do your work here

create()
db_connection = db()


#def startScrapperSchdular():
#    print(db_connection)
#    print ("test")
#    logger.debug("startScrapper")
#    scheduler1 = BackgroundScheduler(job_defaults={'max_instances': config["MaxNInstance"]})
#    # scheduler1.add_job(id='Scheduled task', func=prr,minute='46', trigger="interval",)
#    scheduler1.add_job(id='Scheduled task', func=startScrapper, seconds=60*60*24, trigger="interval")
#    scheduler1.start()
#    atexit.register(lambda: scheduler1.shutdown())
#    print("Scrapper tarted Again !!!!!")
#
#
#def startScrapper():
#    logger.debug("startScrapper")
#    bashCommand = "python3 main_linux.py"
#    os.system(bashCommand)
#
#
#app.before_first_request(startScrapperSchdular)


@app.errorhandler(werkzeug.exceptions.HTTPException)  # werkzeug error handler
def Error(err):
    logger.error(
        'HTTPException Error')

    return error(err.name, err.code)


@app.route('/',methods = ['POST', 'GET'])
def home():
    return respon("ok")


def error(name, code):  # format error massage and returns flask response
    logger.error(
        f'\nError(name, code)->-----------name {name}   code {code}\n')

    obj = {
        "status": code,
        "error": name,
        "powerdby": "Devcorps"
    }
    return flask.Response(status=code, response=json.dumps(obj))


def respon(data):  # format error massage and returns flask response
    obj = {
        "status": "200",
        "data": data,
        "powerdby": "Devcorps"
    }
    return flask.Response(status=200, response=json.dumps(obj))


@app.route('/getData',methods = ['POST', 'GET'])
def getData():
    key = request.args.get('key')
    valid = isvalid(key)
    if not valid:
        return error("Bad Request", 400)
    pname = request.args.get('ProductName')
    q = {
        'query': 'Product Name',
        'value': pname,
        'flag' : True
    }
    dataList = db_connection.select('Product_prices', True, q)
    return respon(dataList)

@app.route('/getTableData',methods = ['POST', 'GET'])
def getTableData():
    key = request.args.get('key')
    valid = isvalid(key)
    if not valid:
        return error("Bad Request", 400)
    fName = ''
    fName = request.args.get('ProductName')
    q = {
        "query": fName,
        'flag' : False
    }
    dataList = db_connection.select('Product_prices', True, q)
    return respon(dataList)


@app.route('/updateData',methods = ['POST', 'GET'])
def updateData():
    key = request.headers.get("key")
    valid = isvalid(key)
    if not valid:
        return error("Bad Request", 400)
    url = "http://188.166.181.245:3575/updateData"
    r = requests.get(url = url, headers={'key': 'MyApiKEy'})

    return str(r)


@app.route('/stopScrapper',methods = ['POST', 'GET'])
def stopScrapper():
    key = request.headers.get("key")
    valid = isvalid(key)
    if not valid:
        return error("Bad Request", 400)
    url = "http://188.166.181.245:3575/stopScrapper"
    r = requests.get(url = url, headers={'key': 'MyApiKEy'})

    return  str(r)
