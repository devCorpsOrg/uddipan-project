from loguru import logger
from log import * 
import random 
from apscheduler.schedulers.background import BackgroundScheduler


i = 0
def prr():
    global i
    logger.debug(f"looggggsss printing : {i}")
    i = i + 1


def isvalid(key):
    if key == "MyApiKEy":
        return True
    else:
        return False


