import SerialControl
import WriteLog
import time
import os

class SerialPortTest(object):
    SERIALPORTCMD = "cd .."
    DETECTIONMAXTIME = 30
    def __init__(self):
        self.serialControl = SerialControl.SerialControl()
        self.writeLog = WriteLog.WriteLog()
    def __getSerialPortData(self):
        startTime = time.time()
        index = 0
        dataResult = []
        self.writeLog.getProcessHandle("SerialPortTest")
        self.serialControl.serialWrite(self.SERIALPORTCMD)
        while True:
            self.serialControl.serialWrite(self.SERIALPORTCMD)
            
            receivedata = self.serialControl.serialReadLine()
            print(receivedata)
            if '#' in receivedata:
                self.writeLog.writeProcessLog(receivedata)
                dataResult.append("1")
            if time.time() - startTime > self.DETECTIONMAXTIME:
                break
        self.serialControl.stopConnect()
        self.writeLog.closeProcessLogHandle()
        return dataResult
    def startSerialPortTest(self):
        dataResult = self.__getSerialPortData()
        if "1" not in dataResult:
            testResult = "FAIL"
        else:
            testResult = "PASS"
        self.writeLog.writeResultLog("SerialPortTest", testResult)
        return testResult
if __name__ == "__main__":
    serialPorttest = SerialPortTest()
    testResult = serialPorttest.startSerialPortTest()
    print("testResult>>",testResult)
