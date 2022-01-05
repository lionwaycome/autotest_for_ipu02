import ETHData
import  TJP
import threading
from ctypes import *
import time
import msgHead
import WriteLog
import SerialControl

class ETHLDForTjp(object):
       MAXTESTTIME  = 30
       TJPSWITCHON = "/svp/etc/appdbg.sh tjpswitch1"
       TJPSWITCHOFF = "/svp/etc/appdbg.sh tjpswitch0"
       def __init__(self):
              self.serialControlHandle = SerialControl.SerialControl()
              self.serialControlHandle.serialWrite(self.TJPSWITCHON)
              self.writeLog = WriteLog.WriteLog()
              self.ethDataHandle = ETHData.EthTest()
              self.ethDataHandle.EthTextMain()
              self.tjpIndex = 0
       def getTjpData(self,tjpData):
              tjpdata = TJP.AppTjpResponseEx()
              memmove(addressof(tjpdata),tjpData,sizeof(TJP.AppTjpResponseEx))
              lineColor_L = tjpdata.appTjpResponse.lineColor_L
              lineColor_R = tjpdata.appTjpResponse.lineColor_R
              self.writeLog.writeProcessLog("tjpdata>>"+"lineColor_L:"+str(lineColor_L)+" lineColor_R:"+str(lineColor_R))
              #print("Vehicle>>",[fls,frs,rls,rrs,speed])
              if 0<lineColor_L<4  or 0<lineColor_R<4:
                     self.tjpIndex += 1
              else:
                     self.tjpIndex = 0
       def dataAnaly(self):
              msghead = msgHead.MsgHead()
              self.writeLog.getProcessHandle("LDForTJP")
              while self.ethDataHandle.runflag:
                     if len(self.ethDataHandle.ALLDATA) > 0:
                            headData = self.ethDataHandle.ALLDATA[0][0:32]
                            memmove(addressof(msghead),headData,sizeof(msgHead.MsgHead))
                            if msghead.msgType == msgHead.AutoBoxMsgType.E_TJP_DATA_BOX.value:
                                   self.getTjpData(self.ethDataHandle.ALLDATA[0][32:])
                            #print(msghead.msgType)
                            del self.ethDataHandle.ALLDATA[0]
       def resultAnaly(self):
             startTime = time.time()
             tjpre = False
             while True:
                if self.tjpIndex > 20:
                    tjpre = True
                    break
                endTime = time.time()
                if endTime - startTime > self.MAXTESTTIME:
                    break
             self.ethDataHandle.runflag = False
             if tjpre:
                return "PASS"
             else:
                return "FAIL"
       def startTest(self):
            
            t1 = threading.Thread(target = self.dataAnaly)
            t1.setDaemon(True)
            t1.start()
            result = self.resultAnaly()
            self.writeLog.closeProcessLogHandle()
            self.writeLog.writeResultLog("LDForTJP",result)
            self.serialControlHandle.serialWrite(self.TJPSWITCHOFF)
            return result
if __name__ == "__main__":
       ethTjp = ETHLDForTjp()
       result = ethTjp.startTest()
       print("TestResult",result)
