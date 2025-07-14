import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime
from dotenv import load_dotenv

def load_logger(name='app_logger',
                console_level=logging.INFO,
                file_level=logging.DEBUG,
                max_bytes=5*1024*1024,
                backup_count=3):
    load_dotenv()

    log_dir = os.getenv('LOGGING_DIR', 'logs')
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f'app_{timestamp}.log')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    ch.setFormatter(formatter)

    fh = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    fh.setLevel(file_level)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


log = load_logger()
