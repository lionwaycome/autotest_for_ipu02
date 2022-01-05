import SerialControl
import WriteLog
import time

class PDFrameTest(object):
       PDSWITCON = "/svp/etc/appdbg.sh pdswitch1"
       PDSWITCOFF = "/svp/etc/appdbg.sh pdswitch0"
       LOGCMD = "cat /storage/stdout.log"
       SENDMSG = "Front_PD ...   FPSG"
       DETECTIONMAXTIME = 120 # uint seconds
       ALLOWABLEMINVALUE = 10
       def __init__ (self):
              # Create a serial object
              self.serialControl = SerialControl.SerialControl()
              self.writeLog = WriteLog.WriteLog()
       def startPDFrameDetection(self):
             self.serialControl. serialWrite(self.PDSWITCON)
             time.sleep(0.5)
             self.serialControl. serialWrite(self.LOGCMD)
             startTime = time.time()
             self.writeLog.getProcessHandle("PDFrameTestDetection")
             frameValue = []
             while True:
                    receivedata = self.serialControl.serialReadLine()
                    if self.SENDMSG in receivedata:
                           receivedata = receivedata.replace("\n","")
                           receivedata = receivedata.replace("\r","")
                           self.writeLog.writeProcessLog(receivedata)
                           print("receiveData>>",receivedata)
                           try:
                                  fps = float(receivedata.split(" ")[-1])
                                  frameValue.append(fps)
                           except:
                                  pass
                    if time.time() - startTime > self.DETECTIONMAXTIME:
                           break
             if len(frameValue) <= 1:
                 testResult = "FAIL;NO data."
             else:
                 if min(frameValue[1:]) < self.ALLOWABLEMINVALUE:
                     testResult = "FAIL;min value:" + str(min(frameValue[1:]))
                 else:
                     testResult = "PASS"
             self.serialControl.fallBack()
             self.serialControl.serialWrite(self.PDSWITCOFF)
             self.serialControl.stopConnect()
             self.writeLog.closeProcessLogHandle()
             self.writeLog.writeResultLog("PDFrameTestDetection",testResult)
             #print("testResult",testResult)
             return testResult 
if __name__ == "__main__":
       pdFrameDetection = PDFrameTest()
       testResult = pdFrameDetection.startPDFrameDetection()
       print("test result:",testResult)
              
                     
       
