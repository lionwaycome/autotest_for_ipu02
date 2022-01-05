import OSVersion
import MCUVersion
import sys
import WriteLog
import writeTXT

def startVersionTest():
    mcuVersion = MCUVersion.MCUVersion()
    mcuResult = mcuVersion.getMCUVersion()
    osVersion = OSVersion.OSVersion()
    osResult,result = osVersion.getOSVersion()
    writeLog = WriteLog.WriteLog()
    if mcuResult and osResult:
        testtoalre = "PASS"
    else:
        testtoalre = "FAIL"
    writeLog.writeResultLog("IPU02_Version",testtoalre+result)
    writeTXT.WriteTXT(result)
    return testtoalre
if __name__ == "__main__":
    result = startVersionTest()
    print("result",result)
