import logging

class LogGenerator:
    @staticmethod
    def loggenerator():
        fhandler = logging.FileHandler(filename="C:/PycharmProjects/nopcommerceApp/Logs/automation.log", mode="a")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger