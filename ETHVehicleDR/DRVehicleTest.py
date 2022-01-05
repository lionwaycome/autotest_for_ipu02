import ETHData
import Vehicle
import IMU
import CtrAlgOut
import threading
from ctypes import *
import time
import msgHead
import WriteLog

class ETHDRVehicle(object):
       MAXTESTTIME  = 60
       def __init__(self):
              self.writeLog = WriteLog.WriteLog()
              self.ethDataHandle = ETHData.EthTest()
              self.ethDataHandle.EthTextMain()
              self.vehicleIndex = 0
              self.drIndex = 0
              self.imuIndex =  0
       def getVehicleData(self,vehicleData):
              vehicledata = Vehicle.VehicleData()
              memmove(addressof(vehicledata),vehicleData,sizeof(Vehicle.VehicleData))
              speed = vehicledata.vehicle_speed
              fls = vehicledata.vehicle_front_left_wheel_pulse
              frs = vehicledata.vehicle_front_right_wheel_pulse
              rls = vehicledata.vehicle_rear_left_wheel_pulse
              rrs = vehicledata.vehicle_rear_right_wheel_pulse
              self.writeLog.writeProcessLog("VehicleData>>"+"fls:"+str(fls)+" frs:"+str(frs)+" rls:"+str(rls)+" rrs:"+str(rrs)+" speed:"+str(speed))
              #print("Vehicle>>",[fls,frs,rls,rrs])
              if fls and frs and rls and rrs:
                     self.vehicleIndex += 1
##              else:
##                     self.vehicleIndex = 0
       def getDRData(self,drData):
              ctrAlgOut = CtrAlgOut.stCtrAlgOut2Mcu()
              memmove(addressof(ctrAlgOut),drData,sizeof(CtrAlgOut.stCtrAlgOut2Mcu))
              dr_x = ctrAlgOut.PosX
              dr_y = ctrAlgOut.PosY
              dr_angle = ctrAlgOut.PosAng
              self.writeLog.writeProcessLog("DRData>>"+"x:"+str(dr_x)+" y:"+str(dr_y)+" yaw:"+str(dr_angle))
              #print("DR>>",[dr_x,dr_y,dr_angle])
              if dr_x >0 and dr_y > 0 and dr_angle >0:
                     self.drIndex += 1
##              else:
##                     self.drIndex = 0
       def getImuData(self,imuData):
              imu = IMU.ImuData()
              memmove(addressof(imu),imuData,sizeof(IMU.ImuData))
              imu_Wx = imu.Wx
              imu_Wy = imu.Wy
              imu_Wz = imu.Wz
              imu_Ax = imu.Ax
              imu_Ay = imu.Ay
              imu_Az = imu.Az
              imu_Alrx = imu.Alrx
              imu_Alry = imu.Alry
              imu_Alrz = imu.Alrz
              self.writeLog.writeProcessLog("IMU>>"+"Wx:"+str(imu_Wx)+" Wy:"+str(imu_Wy)+" Wz:"+str(imu_Wz)+\
                                            " imu_Ax:"+str(imu_Ax)+" imu_Ay:"+str(imu_Ay)+" imu_Az:"+str(imu_Az)+\
                                             " imu_Alrx:"+str(imu_Alrx)+" imu_Alry:"+str(imu_Alry)+" imu_Alrz:"+str(imu_Alrz))
              if imu_Wx and imu_Wy and imu_Wz:
                     self.imuIndex += 1
                     
##              else:
##                     self.imuIndex = 0
              print(imu_Wx,imu_Wy,imu_Wz,self.imuIndex)
       def dataAnaly(self):
              msghead = msgHead.MsgHead()
              self.writeLog.getProcessHandle("DRVehivle")
              while self.ethDataHandle.runflag:
                     if len(self.ethDataHandle.ALLDATA) > 0:
                            headData = self.ethDataHandle.ALLDATA[0][0:32]
                            memmove(addressof(msghead),headData,sizeof(msgHead.MsgHead))
                            if msghead.msgType == msgHead.AutoBoxMsgType.E_VEHICLE_DATA_BOX.value:
                                   self.getVehicleData(self.ethDataHandle.ALLDATA[0][32:])
                            if msghead.msgType == msgHead.AutoBoxMsgType.E_CTRLALG_OUT_FROM_MCU_BOX.value:
                                   self.getDRData(self.ethDataHandle.ALLDATA[0][32:])
                            if msghead.msgType == msgHead.AutoBoxMsgType.E_IMU_FROM_MCU_BOX.value:
                                   self.getImuData(self.ethDataHandle.ALLDATA[0][32:])
                            #print(msghead.msgType)
                            del self.ethDataHandle.ALLDATA[0]
       def resultAnaly(self):
             startTime = time.time()
             vehiclere = False
             drresult = False
             imuresult = False
             while True:
                if self.drIndex > 20:
                    drresult = True
                if self.vehicleIndex >20:
                    vehiclere = True
                if self.imuIndex > 20:
                       imuresult = True
                if drresult and vehiclere and imuresult:
                        break
                endTime = time.time()
                if endTime - startTime > self.MAXTESTTIME:
                    break
             self.ethDataHandle.runflag = False
             if vehiclere and drresult and imuresult:
                return "PASS"
             else:
                return "FAIL"
       def startTest(self):
            t1 = threading.Thread(target = self.dataAnaly)
            t1.setDaemon(True)
            t1.start()
            result = self.resultAnaly()
            self.writeLog.closeProcessLogHandle()
            self.writeLog.writeResultLog("DRVehicle",result)
            return result
if __name__ == "__main__":
       ethVehicle = ETHDRVehicle()
       result = ethVehicle.startTest()
       print("TestResult",result)
