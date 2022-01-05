import SerialControl
import WriteLog
import time

class CSDDetection(object):
       LOGCMD = "cat /storage/stdout.log"
       SENDMSG = "send msg csd result"
       DETECTIONMAXTIME = 120 # uint seconds
       def __init__ (self):
              # Create a serial object
              self.serialControl = SerialControl.SerialControl()
              self.writeLog = WriteLog.WriteLog()
       def signleTest(self):
             self.serialControl.serialWrite(self.LOGCMD)
             startTime = time.time()
             
             while True:
                    receivedata = self.serialControl.serialReadLine()
                    if self.SENDMSG in receivedata:
                           receivedata = receivedata.replace("\n","")
                           receivedata = receivedata.replace("\r","")
                           self.writeLog.writeProcessLog(receivedata)
                           print("receivedata>> ",receivedata)
                           if "1" in receivedata:
                                  testResult = "PASS"
                                  break
                    if time.time() - startTime > self.DETECTIONMAXTIME:
                           testResult = "FAIL"
                           break
             return testResult
       def startCSDDetection(self):
             indexFlag = 0
             self.writeLog.getProcessHandle("CSDDetection")
             while indexFlag < 3:
                    print("indexFlag>>",indexFlag)
                    testResult = self.signleTest()
                    print(testResult)
                    if testResult == "PASS":
                           break
                    indexFlag += 1
             
             self.writeLog.closeProcessLogHandle()
             self.writeLog.writeResultLog("CSDDetection",testResult)
             self.serialControl.stopConnect()
             return testResult 
if __name__ == "__main__":
       csdDetection = CSDDetection()
       csdDetection.startCSDDetection()
              
                     
       
