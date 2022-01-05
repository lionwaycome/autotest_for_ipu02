import SerialControl
import WriteLog
import time
import frameResult


class RPPFrameTest(object):
    LOGCMD = "cat /storage/stdout.log"
    SENDMSG = "APA << DetectionTask Check  Left  FPS"
    ENTERPARKING = "/svp/etc/appdbg.sh apa3"
    EXITRKING =    "/svp/etc/appdbg.sh apa1"
    DETECTIONMAXTIME = 120  # uint seconds
    MEANVLUE = 14
    MINVALUE = 10
    CONTINUEVALUE = 14
    def __init__(self):
        # Create a serial object
        self.serialControl = SerialControl.SerialControl()
        self.writeLog = WriteLog.WriteLog()
    def startRPPFrameDetection(self):
        self.serialControl.serialWrite(self.ENTERPARKING)
        time.sleep(1)
        self.serialControl.serialWrite(self.LOGCMD)
        startTime = time.time()
        self.writeLog.getProcessHandle("RPPFrameTestDetection")
        frameValue = []
        while True:
            receivedata = self.serialControl.serialReadLine()
            #print(receivedata)
            if self.SENDMSG in receivedata:
                receivedata = receivedata.replace("\n", "")
                receivedata = receivedata.replace("\r", "")
                self.writeLog.writeProcessLog(receivedata)
                #print(receivedata)
                fps = receivedata.split(self.SENDMSG)[-1].strip().split(" ")[0]
                print("APA Detection>>",fps)
                try:
                    fps = float(fps[:-1])
                    frameValue.append(fps)
                except:
                    pass
                
            if time.time() - startTime > self.DETECTIONMAXTIME:
                break
        if len(frameValue) <= 0:
            testResult = "FAIL;No Data."
        else:
            testResult = frameResult.frameResult(frameValue, self.MEANVLUE, self.MINVALUE, self.CONTINUEVALUE)
        self.serialControl.fallBack()
        self.serialControl.serialWrite(self.EXITRKING)
        time.sleep(1)
        self.serialControl.stopConnect()
        self.writeLog.closeProcessLogHandle()
        self.writeLog.writeResultLog("RPPFrameTestDetection", testResult)
        return testResult
if __name__ == "__main__":
    rppFrameDetection = RPPFrameTest()
    testResult = rppFrameDetection.startRPPFrameDetection()
    print(testResult)
    
