import threading
import USS
import ETHData
from ctypes import *
import time
import msgHead
import WriteLog
import sys

MAXTESTTIME = 30
MAXTESTNUM = 10


def USSTest(data):
    ussData = USS.MavpUltrasonicData()
    memmove(addressof(ussData),data,sizeof( USS.MavpUltrasonicData))
    ussdistace = [ussData.USS_RRStx_RRSrx,ussData.USS_RRtx_RRrx,ussData.USS_RRMtx_RRMrx,ussData.USS_RLMtx_RLMrx,ussData.USS_RLtx_RLrx,ussData.USS_RLStx_RLSrx,\
                 ussData.USS_FRStx_FRSrx, ussData.USS_FRtx_FRrx,ussData.USS_FRMtx_FRMrx,ussData.USS_FLMtx_FLMrx,ussData.USS_FLtx_FLrx,ussData.USS_FLStx_FLSrx]
    WriteLog.writefile("USSDistance",str(ussdistace)+"\n")
    #print(ussdistace)
    if 0 in ussdistace:
        return False
    elif 32767 in ussdistace:
        return False
    elif 5000 in ussdistace:
        return False
    elif 2500 in ussdistace:
        return False
    else:
        return True
def analyData(ethData):
    msghead = msgHead.MsgHead()
    indexflag = 0
    starttime = time.time()
    testResult = "PASS"
    while True:
        if len(ethData.ALLDATA) > 0:
            data = ethData.ALLDATA[0][0:32]
            memmove(addressof(msghead),data,sizeof(msgHead.MsgHead))
            if msghead.TagLen != len(ethData.ALLDATA[0])-32:
                pass
            else:
                if msghead.msgType == msgHead.AutoBoxMsgType.E_ULTRASONIC_DATA_BOX.value:
                        if USSTest(ethData.ALLDATA[0][32:]):
                            indexflag += 1
            del ethData.ALLDATA[0]
            if indexflag >MAXTESTNUM:
                testResult = "PASS"
                ethData.runflag = False
                break
        if time.time() - starttime > MAXTESTTIME:
                ethData.runflag = False
                testResult = "FAIL"
                break
    return testResult
def StartTest():
    ethTest = ETHData.EthTest("198.18.36.100",5008)
    t3 = threading.Thread(target=ethTest.EthTextMain)
    #t4 = threading.Thread(target=analyData,args=(ethTest,))
    t3.setDaemon(True)
    #t4.setDaemon(True)
    t3.start()
    testResult = analyData(ethTest)
##    return testResult
    sys.stdout.write(testResult)
    #print(testResult)
   # t4.start()
if __name__ == "__main__":
    StartTest()
    
