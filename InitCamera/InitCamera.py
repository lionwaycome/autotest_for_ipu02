import SerialControl
import WriteLog
import time
CMD0 = "cp -rvf /sd/nl5_calib/picture_library/*  /svp/etc/NL-5/picture_library/"
CMD1 = "cp -rvf /sd/nl5_calib/calib_pattern/*  /svp/etc/NL-5/params/calib_pattern/"
CMD2 = "cp -rvf /sd/nl5_calib/calib_pattern/calibration_params.xml  /svp/etc/NL-5/goldendata/calibration_params_default.xml"
CMD3 = "rm -rf /svp/cache/*"
CMD4 = "rm -rf /var/avm/calibrationBK"
CMD5 = "sync"
CMD = [CMD0,CMD1,CMD2,CMD3,CMD4,CMD5]
class InitCamera(object):

       DETECTIONMAXTIME = 20 # uint seconds
       def __init__ (self):
              # Create a serial object
              self.serialControl = SerialControl.SerialControl()
              self.writeLog = WriteLog.WriteLog()
       def startInitCamera(self):
            for cmd in CMD:
                self.serialControl. serialWrite(cmd) 
                time.sleep(5)
            self.serialControl.stopConnect() 
if __name__ == "__main__":
       initCam = InitCamera()
       initCam.startInitCamera()
              
                     
       
