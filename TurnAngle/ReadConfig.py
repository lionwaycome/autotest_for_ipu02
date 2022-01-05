import configparser
#import os

class ReadConfig(object):
    def __init__(self):
        self.getAbsPath()
        self.readconfig()
        self.serialCOM()
        self.writeLog()
        self.detectionCamera()
        self.ETHConfig()
    def getAbsPath(self):
        abs_file=__file__
        self.absPath=abs_file[:abs_file.rfind("\\")]
    def readconfig(self):
        configpath ="D:\\TestStand_IPU02\\dist\\config\\Config.ini"
        self.configINI = configparser.ConfigParser()
        self.configINI.read(configpath)
    def serialCOM(self):
        self.comNum = self.configINI.get("SERIALCOM", "comNum")
    def writeLog(self):
        self.writeLogPath = self.configINI.get("WRITELOG", "writelogpath")
    def detectionCamera(self):
        self.detectionCameraNum = self.configINI.get("DETECTIONCAMERA", "cameranum")
    def ETHConfig(self):
        self.IPAddress = self.configINI.get("ETHCONFIG", "IP")
        self.ETHPortNum = self.configINI.get("ETHCONFIG", "portNum")
if __name__ == "__main__":
    readConfig = ReadConfig()
    #readConfig.serialCOM()
    print(readConfig.detectionCameraNum)
