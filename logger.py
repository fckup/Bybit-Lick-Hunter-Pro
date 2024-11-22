import logging

def setup_logger():
    logger = logging.getLogger('bybit_lick_hunter')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('bybit_lick_hunter.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
