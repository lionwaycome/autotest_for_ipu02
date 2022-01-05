import SerialControl
import WriteLog
import time


class TJPFrameTest(object):
    TJPSWITCON = "/svp/etc/appdbg.sh tjpswitch1"
    TJPSWITCOFF = "/svp/etc/appdbg.sh tjpswitch0"
    LOGCMD = "cat /storage/stdout.log"
    SENDMSG = "TJP << FPS"
    DETECTIONMAXTIME = 60  # uint seconds
    ALLOWABLEMINVALUE = 15

    def __init__(self):
        # Create a serial object
        self.serialControl = SerialControl.SerialControl()
        self.writeLog = WriteLog.WriteLog()

    def startTJPFrameDetection(self):
        self.serialControl.fallBack()
        self.serialControl.serialWrite(self.TJPSWITCON)
        time.sleep(0.5)
        self.serialControl.serialWrite(self.LOGCMD)
        startTime = time.time()
        self.writeLog.getProcessHandle("TJPFrameTestDetection")
        frameValue = []
        while True:
            receivedata = self.serialControl.serialReadLine()
            print("receivedata>>",receivedata)
            if self.SENDMSG in receivedata:
                receivedata = receivedata.replace("\n", "")
                receivedata = receivedata.replace("\r", "")
                self.writeLog.writeProcessLog(receivedata)
                print(receivedata)
                fps = receivedata.split(SENDMSG)[-1].strip().split(" ")[0]
                try:
                    fps = float(fps[:-1])
                except:
                    pass
                frameValue.append(fps)
            if time.time() - startTime > self.DETECTIONMAXTIME:
                break
        if len(frameValue) <= 0:
            testResult = "FAIL;NO data."
        else:
            if min(frameValue) < self.ALLOWABLEMINVALUE:
                testResult = "FAIL;min value:"+str(min(frameValue))
            else:
                testResult = "PASS"
        self.serialControl.fallBack()
        self.serialControl.serialWrite(self.TJPSWITCOFF)
        self.serialControl.stopConnect()
        self.writeLog.closeProcessLogHandle()
        self.writeLog.writeResultLog("TJPFrameTestDetection", testResult)
        return testResult
if __name__ == "__main__":
    tjpFrameDetection = TJPFrameTest()
    testResult = tjpFrameDetection.startTJPFrameDetection()
    print("testResult>>",testResult)
