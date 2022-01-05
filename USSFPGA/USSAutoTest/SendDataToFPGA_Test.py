#! /usr/env python

# -- coding:utf-8 --

# Date: 2021/8/12 10:47

# Author: Feng Manyi

# PyFile: SendDataToFPGA.py
import time

import ReadConfig
import UDP_ReceiveUSSData
import serial
import struct
import threading

class SendDataToFPGA(object):
    def __init__(self,serverIP,serverPortNum,ClientIP,ClientPortNum):
        self.udpReceive = UDP_ReceiveUSSData.UDPReceive(serverIP,int(serverPortNum),ClientIP,int(ClientPortNum))
        self.USSData = []
        self.stopFlag = False
    def getComNumAndConnect(self):
        readConfig = ReadConfig.ReadConfig()
        serialNum = [readConfig.F123,readConfig.F456,readConfig.R123,readConfig.R456]
        self.serialHandle = []
        for itemdata in serialNum:
            returndata = self.creatseialHandle(itemdata)
            if returndata:
                print(itemdata, "connect sucess.")
                self.serialHandle.append(returndata)
            else:
                self.udpReceive.runflag = False
                print(itemdata, "connect fail.")
                break
    def creatseialHandle(self,comportNum):
        try:
            serHandle=serial.Serial(comportNum)
            serHandle.baudrate=9600
            serHandle.timeout=5
            return serHandle
        except:
            return False
    def stopConnect(self):
        for itemdata in self.serialHandle:
            itemdata.close()
    def sendDataToFpga(self,sendData,serialIndex):
        itemdata1 = int(float(sendData[0])*1000000)
        itemdata2 = int(float(sendData[1])*1000000)
        itemdata3 = int(float(sendData[2])*1000000)
        #print(sendData)
        print(itemdata1,itemdata2,itemdata3)
        bufferData = struct.pack(">HHH", itemdata1, itemdata2,itemdata3)
        self.serialHandle[serialIndex].write(bufferData)
        #time.sleep(0.01)
    def getUSSLongDistance(self,data):
        dis = float(data)*170
        if 0 < dis < 5:
            return dis
        else:
            return 5
    def dataAnalyToFpga(self,data):
        x = [[data[8],data[7],data[6]], [data[9],data[11],data[10]],[data[5],data[3],data[4]],[data[2],data[0],data[1]]]
        self.sendDataToFpga(x[0],0)
        self.sendDataToFpga(x[1],1)
        self.sendDataToFpga(x[2],2)
        self.sendDataToFpga(x[3],3)
        for index in range(4):
            senddatatime =x[index]
            #print("senddatatime>>",senddatatime,">>end")
            self.sendDataToFpga(senddatatime,index)
    def ussDataAnalyAndSendToFpga(self):
        print("Send data to fpga.")
        self.stopFlag = True
        self.udpReceive.UDPReceiveMain()
        self.getComNumAndConnect()
        while self.stopFlag:
            if len(self.udpReceive.originData) > 0:
                oriData = self.udpReceive.originData[-1]
                self.dataAnalyToFpga(oriData)
                self.udpReceive.originData = []
            else:
                pass
        self.udpReceive.closeUdpHandle()
        print("Stop send data to fpga.")
    def startTest(self):
        t1 = threading.Thread(target = self.ussDataAnalyAndSendToFpga)
        t1.start()
if __name__ == "__main__":
    sendDataToFpga = SendDataToFPGA("127.0.0.1",9996,"127.0.0.1",11205)
    sendDataToFpga.ussDataAnalyAndSendToFpga()
    print("START")
