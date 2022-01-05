import SerialControl
import WriteLog
import CameraDetection
import time

class BAFDetection(object):
       OPENBAF = "/svp/etc/appdbg.sh bfswitch1"
       CLOSEBAF = "/svp/etc/appdbg.sh bfswitch0"
       def __init__ (self):
              # Create a serial object
              self.serialControl = SerialControl.SerialControl()
              self.writeLog = WriteLog.WriteLog()
              self.openBAF()
              self.camerDetection = CameraDetection.CameraDetection([0, 0, 221],[180, 30, 251],[270,365,155,195],600)
       def openBAF(self):
              self.serialControl.serialWrite(self.OPENBAF)
       def closeBAF(self):
              self.serialControl.serialWrite(self.CLOSEBAF)
              self.serialControl.stopConnect()
       def startMain(self):
              result = self.camerDetection.startDetection()
              self.writeLog.writeResultLog("BAFDetection",result)
              self.closeBAF()
              return result
if __name__ == "__main__":
       bafDetection = BAFDetection()
       result = bafDetection.startMain()
       print(result)
       #time.sleep(10)
      #bafDetection.closeBAF()
              

                     
       
