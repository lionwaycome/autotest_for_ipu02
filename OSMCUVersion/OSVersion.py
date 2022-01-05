#! /usr/env python

# -- coding:utf-8 --

# Date: 2021/8/25 16:06

# Author: Feng Manyi

# PyFile: OSVersion.py

import SerialControl
import WriteLog
import time
import datetime

class OSVersion(object):
       OSDATA = "cat /version/version.sh"
       OSVersion = ["OS_VERSION=","MAIN_VERSION=","BSP_VERSION="]
       def __init__(self):
              self.serialControl = SerialControl.SerialControl()
              self.writeLog = WriteLog.WriteLog()
              self.osversionData = []
       def __OSVersionResult(self):
              currentTime = "IPU02_OS_"+time.strftime("%Y%m%d", time.localtime(time.time()))[2:]
              if len(self.osversionData) == 0:
                     return False,"NO DATA"
              else:
                     testResult = False
                     OSResult = ""
                     for item in self.osversionData:
                            if currentTime in item:
                                   testResult = True
                            item = item.replace("\r", "")
                            item = item.replace("\n", "")
                            OSResult += item + ";"
              return testResult,OSResult
       def getOSVersion(self):
              self.serialControl.serialWrite(self.OSDATA)
              startTime = time.time()
              self.writeLog.getProcessHandle("Version")
              while True:
                     receivedata = self.serialControl.serialReadLine()
                     for itemdata in self.OSVersion:
                            if itemdata in receivedata:
                                   self.osversionData.append(receivedata)
                                   self.writeLog.writeProcessLog(receivedata)
                                   break
                     if "export OS_VERSION MAIN_VERSION BSP_VERSION" in receivedata:
                         break
                     if time.time() - startTime > 10:
                            break
              self.serialControl.stopConnect()
              self.writeLog.closeProcessLogHandle()
              return self.__OSVersionResult()
if __name__ == "__main__":
    print("START")
