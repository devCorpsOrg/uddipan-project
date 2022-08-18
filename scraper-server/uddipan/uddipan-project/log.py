from loguru import logger
import time
import sys
from config import config

log_dir = config["LogFolder"]
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add(f"{log_dir}/logs_{time.time()}.log", enqueue=True, rotation="12:00")

