import SerialControl
import WriteLog
import time
import os


class ETHPingTest(object):
    DUTPINGPCCMD = "ping 198.18.36.100"
    DETECTIONMAXTIME = 30
    def __init__(self):
        self.serialControl = SerialControl.SerialControl()
        self.writeLog = WriteLog.WriteLog()
    def __PCpingDUT(self):
        PING_RESULT = os.system(u"ping 198.18.36.96")
        if  PING_RESULT == 0:
            result = True
        else:
            result = False
        return result
    def __DUTpingPC(self):
        startTime = time.time()
        result = False
        self.writeLog.getProcessHandle("ETHDUTPingPC")
        self.serialControl.serialWrite(self.DUTPINGPCCMD)
        while True:
            receivedata = self.serialControl.serialReadLine()
            self.writeLog.writeProcessLog(receivedata)
            if 'ttl' in receivedata:
                result = True
                break
            if time.time() - startTime > self.DETECTIONMAXTIME:
                break
        self.serialControl.stopConnect()
        self.writeLog.closeProcessLogHandle()
        return result
    def startETHpingTest(self):
        if self.__DUTpingPC() and self.__PCpingDUT():
            testResult = "PASS"
        else:
            testResult = "FAIL"
        self.writeLog.writeResultLog("ETHPingTest", testResult)
        return testResult
if __name__ == "__main__":
    ethPing = ETHPingTest()
    testResult = ethPing.startETHpingTest()
    print("testResult>>",testResult)
