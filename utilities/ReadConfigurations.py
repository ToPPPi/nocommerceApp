import configparser

config = configparser.RawConfigParser()
config.read("C://PycharmProjects//nopcommerceApp//Configurations//config.ini")

class ReadConfig:
    @staticmethod               #Чтобы не использовать "self", нужно написать @staticmethod.
    def getApplicationgURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password