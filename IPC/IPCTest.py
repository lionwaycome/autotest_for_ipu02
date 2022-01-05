import SerialControl
import WriteLog
import time
import os

resultplay = ["0xdead0000","0xdead0001","0xdead0002","0xdead0003",
              "0xdead0004","0xdead0005","0xdead0006","0xdead0007",
              "0xdead0008","0xdead0009","0xdead000a","0xdead000b",
              "0xdead000c","0xdead000d","0xdead000e","0xdead000f"]
class IPCTest(object):
    IPCCMD = "./vision_apps/vx_app_qnx_arm_ipc.out"
    DETECTIONMAXTIME = 6
    def __init__(self):
        self.serialControl = SerialControl.SerialControl()
        self.writeLog = WriteLog.WriteLog()
    def __getIPCData(self):
        startTime = time.time()
        index = 0
        dataResult = []
        self.writeLog.getProcessHandle("IPCTest")
        self.serialControl.serialWrite(self.IPCCMD)
        while True:
            receivedata = self.serialControl.serialReadLine()
            #print(receivedata)
            if '0xdead000' in receivedata:
                self.writeLog.writeProcessLog(receivedata)
                dataResult.append("0xdead000"+receivedata[9])
            if time.time() - startTime > self.DETECTIONMAXTIME:
                break
        self.serialControl.stopConnect()
        self.writeLog.closeProcessLogHandle()
        for re in dataResult:
            print(re)
            if re in resultplay:
                index += 1
        return index
    def startIPCTest(self):
        indexResult = self.__getIPCData()
        #print(indexResult)
        if indexResult > 15:
            testResult = "PASS"
        else:
            testResult = "FAIL"
        self.writeLog.writeResultLog("IPCTest", testResult)
        return testResult
if __name__ == "__main__":
    ipctest = IPCTest()
    testResult = ipctest.startIPCTest()
    print("testResult>>",testResult)
