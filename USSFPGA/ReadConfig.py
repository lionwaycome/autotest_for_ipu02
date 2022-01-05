import configparser
import os

class ReadConfig(object):
    def __init__(self):
        self.getAbsPath()
        self.readconfig()
        self.serialCOM()
    def getAbsPath(self):
        self.absPath=os.path.abspath(".")
    def readconfig(self):
        configpath = self.absPath+ "\\Config.ini"
        self.configINI = configparser.ConfigParser()
        self.configINI.read(configpath)
    def serialCOM(self):
        self.F123 = self.configINI.get("SERIALCOM", "F123")
        self.F456 = self.configINI.get("SERIALCOM", "F456")
        self.R123 = self.configINI.get("SERIALCOM", "R123")
        self.R456 = self.configINI.get("SERIALCOM", "R456")
if __name__ == "__main__":
    readConfig = ReadConfig()
    #readConfig.serialCOM()
    print(readConfig.F123)
