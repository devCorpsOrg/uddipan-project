from main import app
from main import db_connection
from loguru import logger
from log import *
import atexit
from CreateDataBase import create
from apscheduler.schedulers.background import BackgroundScheduler


if __name__ == '__main__':    
    app.run(port=3575,host='0.0.0.0', use_reloader=False)