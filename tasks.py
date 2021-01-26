from loguru import logger
from time import sleep

def slow_func(n):
    for i in range(n):
        logger.info(i)
        sleep(1)