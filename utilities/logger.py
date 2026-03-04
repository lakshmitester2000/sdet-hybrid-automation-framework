import logging

def get_logger():
    logger = logging.getLogger()
    if not logger.handlers:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    return logger