import logging

def setup_logging():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        #write logs
        file_handler = logging.FileHandler("bot.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        #console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger