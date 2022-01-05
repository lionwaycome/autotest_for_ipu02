import os
import time
import ReadConfig

class WriteLog(object):
       def __init__(self):
              readConfig = ReadConfig.ReadConfig()
              self.writeLogPath = "D:\\UDP_Autolibrary_Project\\Python\\logdata"#readConfig.writeLogPath
              self.creatFold()
              self.getWriteResultLogHandle()
       def creatFold(self):
              if not os.path.exists(self.writeLogPath):
                     os.makedirs(self.writeLogPath)
       def getWriteResultLogHandle(self):
              datename = time.strftime("%Y%m%d", time.localtime(time.time()))
              self.writeResultLogHandle = open(self.writeLogPath+"\\logResult"+datename+".log","a+")
       def writeResultLog(self,testName,resultData):
              timename = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
              self.writeResultLogHandle.write("*****"*10+testName+"******"*10+"\n")
              self.writeResultLogHandle.write(testName+" ["+timename+"] >> "+resultData+"\n")
              self.writeResultLogHandle.close()
       def getProcessHandle(self,testName):
              timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
              self.writeProcessDataHandle = open(self.writeLogPath+"\\"+testName+timename+".txt","a+")
       def writeProcessLog(self,processData):
              processData = processData.replace("\n","")
              self.writeProcessDataHandle.write(processData+"\n")
       def closeProcessLogHandle(self):
               self.writeProcessDataHandle.close()
if __name__ == "__main__":
       writeLog = WriteLog()
       writeLog.writeResultLog("CSD","PASS")
