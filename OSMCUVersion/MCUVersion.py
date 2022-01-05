import SerialControl
import WriteLog
import time
import datetime

class MCUVersion(object):
       MCUDATA = "cat /storage/stdout.log"
       MCUVersion = ["sysMCU1Version","sysMCU3Version","sysMCU2_1Version","sysMCU2_0Version"]
       def __init__(self):
              self.serialControl = SerialControl.SerialControl()
              self.writeLog = WriteLog.WriteLog()
              self.versionData = []
       def __MCUVersionResult(self):
              currentTime = int(datetime.datetime.now().strftime("%m%d"))
              if len(self.versionData) == 0:
                     return False
              else:
                     for item in self.versionData:
                            if currentTime != item:
                                   return False
              return True
       def getMCUVersion(self):
              self.serialControl.serialWrite(self.MCUDATA)
              startTime = time.time()
              self.writeLog.getProcessHandle("Version")
              while True:
                     receivedata = self.serialControl.serialReadLine()
                     for itemdata in self.MCUVersion:
                            if itemdata in receivedata:
                                   #print(receivedata,receivedata.split("_22")[-1].split("_")[0])
                                   try:
                                          self.versionData.append(int(receivedata.split("_22")[-1].split("_")[0]))
                                   except:
                                          pass
                                   self.writeLog.writeProcessLog(receivedata)
                                   break
                     if time.time() - startTime > 10:
                            break
              self.serialControl.stopConnect()
              self.writeLog.closeProcessLogHandle()
              return self.__MCUVersionResult()
if __name__ == "__main__":
       mcu = MCUVersion()
       res = mcu.getMCUVersion()
       print(res)
