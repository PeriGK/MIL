import logging
from logging.handlers import TimedRotatingFileHandler


# ----------------------------------------------------------------------
def create_hourly_rotating_log(path, log_level):

    logger = logging.getLogger()
    logger.setLevel(log_level)
    log_handler = TimedRotatingFileHandler(path, when="m", interval=60, backupCount=10)
    logger.addHandler(log_handler)