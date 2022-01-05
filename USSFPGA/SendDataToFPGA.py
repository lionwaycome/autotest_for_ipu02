#! /usr/env python

# -- coding:utf-8 --

# Date: 2021/8/12 10:47

# Author: Feng Manyi

# PyFile: SendDataToFPGA.py

import time
import ReadConfig
import serial
import struct

import logging
VEHICLE = 340

class SendDataToFPGA(object):
    def __init__(self):
        self.getComNumAndConnect()
    def getComNumAndConnect(self):
        readConfig = ReadConfig.ReadConfig()
        serialNum = [readConfig.F123,readConfig.F456,readConfig.R123,readConfig.R456]
        self.serialHandle = []
        for itemdata in serialNum:
            returndata = self.creatseialHandle(itemdata)
            if returndata:
                print(itemdata, " connect sucess.")
                self.serialHandle.append(returndata)
            else:
                self.udpReceive.runflag = False
                self.udpReceive.logHandle.error(itemdata+"connect fail.")
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
        self.serialHandle[serialIndex].write(sendData)
    def dataAnalyToFpga(self,data):
        for  index  in range(4):
            bufferData = struct.pack(">HHH", int(data*1000000), int(data*1000000),int(data*1000000))
            self.sendDataToFpga(bufferData,index)
    def sendDataOneMeter(self):
            dataAnalyToFpga(float(1)/170)
    def sendDataZeroMeter(self):
            dataAnalyToFpga(float(0)/170)
if __name__ == "__main__":
    sendDataToFpga = SendDataToFPGA()
    sendDataToFpga.dataAnalyToFpga(float(0)/170)
    print("START")
