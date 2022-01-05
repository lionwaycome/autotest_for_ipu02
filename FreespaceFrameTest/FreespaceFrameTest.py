import SerialControl
import WriteLog
import time
import frameResult

class FSFrameTest(object):
    FSSWITCON = "/svp/etc/appdbg.sh fsswitch1"
    FSSWITCOFF = "/svp/etc/appdbg.sh fsswitch0"
    LOGCMD = "cat /storage/stdout.log"
    SENDMSG = "FS ...   FPSG"
    DETECTIONMAXTIME = 120  # uint seconds
    MEANVLUE = 18
    MINVALUE = 15
    CONTINUEVALUE = 18
    def __init__(self):
        # Create a serial object
        self.serialControl = SerialControl.SerialControl()
        self.writeLog = WriteLog.WriteLog()
    def startFSFrameDetection(self):
        self.serialControl.serialWrite(self.FSSWITCON)
        time.sleep(0.5)
        self.serialControl.serialWrite(self.LOGCMD)
        startTime = time.time()
        self.writeLog.getProcessHandle("FreespaceFrameTestDetection")
        frameValue = []
        while True:
            receivedata = self.serialControl.serialReadLine()
            if self.SENDMSG in receivedata:
                receivedata = receivedata.replace("\n", "")
                receivedata = receivedata.replace("\r", "")
                self.writeLog.writeProcessLog(receivedata)
                print(receivedata)
                try:
                    fps = float(receivedata.split(" ")[-1])
                    frameValue.append(fps)
                except:
                    pass
            if time.time() - startTime > self.DETECTIONMAXTIME:
                break
        if len(frameValue) <= 0:
            testResult = "FAIL;NO Data."
        else:
            testResult = frameResult.frameResult(frameValue,self.MEANVLUE,self.MINVALUE,self.CONTINUEVALUE)
        self.serialControl.fallBack()
        self.serialControl.serialWrite(self.FSSWITCOFF)
        self.serialControl.stopConnect()
        self.writeLog.closeProcessLogHandle()
        self.writeLog.writeResultLog("FreespaceFrameTestDetection", testResult)
        return testResult
if __name__ == "__main__":
    fsFrameDetection = FSFrameTest()
    testResult = fsFrameDetection.startFSFrameDetection()
    print("testResult>>",testResult)
