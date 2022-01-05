import ETHData
import Aps
import threading
from ctypes import *
import time
import msgHead
import WriteLog

class ETHDRVehicle(object):
       MAXTESTTIME  = 120
       def __init__(self):
              self.writeLog = WriteLog.WriteLog()
              self.ethDataHandle = ETHData.EthTest()
              self.ethDataHandle.EthTextMain()
              self.slotIndex = 0
       def getApsData(self,apsData):
              apsdata = Aps.AppApaResponseEx()
              memmove(addressof(apsdata),apsData,sizeof(Aps.AppApaResponseEx))
              a_x = apsdata.appApaResponse.apaTargetSlot.apaSlotA_x
              a_y = apsdata.appApaResponse.apaTargetSlot.apaSlotA_y
              b_x = apsdata.appApaResponse.apaTargetSlot.apaSlotB_x
              b_y = apsdata.appApaResponse.apaTargetSlot.apaSlotB_y
              c_x = apsdata.appApaResponse.apaTargetSlot.apaSlotC_x
              c_y = apsdata.appApaResponse.apaTargetSlot.apaSlotC_y
              d_x = apsdata.appApaResponse.apaTargetSlot.apaSlotD_x
              d_y = apsdata.appApaResponse.apaTargetSlot.apaSlotD_y
              print([a_x,a_y,b_x,b_y,c_x,c_y,d_x,d_y])
              self.writeLog.writeProcessLog("slot>>"+"a_x:"+str(a_x)+" a_y:"+str(a_y)+" b_x:"+str(b_x)+" b_y:"+str(b_y)\
                                            +" c_x:"+str(c_x)+" c_y:"+str(c_y)+" d_x:"+str(d_x)+" d_y:"+str(d_y))
              if 0 not in [a_x,a_y,b_x,b_y,c_x,c_y,d_x,d_y]:
                     self.slotIndex += 1
              else:
                     self.slotIndex = 0
       def dataAnaly(self):
              msghead = msgHead.MsgHead()
              self.writeLog.getProcessHandle("APSSlotParking")
              while self.ethDataHandle.runflag:
                     if len(self.ethDataHandle.ALLDATA) > 0:
                            headData = self.ethDataHandle.ALLDATA[0][0:32]
                            memmove(addressof(msghead),headData,sizeof(msgHead.MsgHead))
                            if msghead.msgType == msgHead.AutoBoxMsgType.E_APA_RESP_BOX.value:
                                   self.getApsData(self.ethDataHandle.ALLDATA[0][32:])
                            del self.ethDataHandle.ALLDATA[0]
       def resultAnaly(self):
             startTime = time.time()
             slotParkingre = False
             while True:
                if self.slotIndex > 20:
                    slotParkingre = True
                    break
                endTime = time.time()
                if endTime - startTime > self.MAXTESTTIME:
                    break
             self.ethDataHandle.runflag = False
             if slotParkingre:
                return "PASS"
             else:
                return "FAIL"
       def startTest(self):
            t1 = threading.Thread(target = self.dataAnaly)
            t1.setDaemon(True)
            t1.start()
            result = self.resultAnaly()
            self.writeLog.closeProcessLogHandle()
            self.writeLog.writeResultLog("APSSlotParking",result)
            return result
if __name__ == "__main__":
       ethVehicle = ETHDRVehicle()
       result = ethVehicle.startTest()
       print("TestResult",result)
