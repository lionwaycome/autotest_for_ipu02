#! /usr/env python

# -- coding:utf-8 --

# Date: 2021/8/12 10:23

# Author: Feng Manyi

# PyFile: UDP_ReceiveUSSData.py

import threading
import socket
import time
import logging
import logger
class UDPReceive(object):
    WAITTIME = 15 #uint ms
    def __init__(self,serverIP,serverPortNum,ClientIP,ClientPortNum):
        self.IP = serverIP#
        self.ReceIP = ClientIP#
        self.PortNum1 = serverPortNum#
        self.PortNum2 = ClientPortNum#
        self.CMDData = b"USS-1"
        self. udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.originData = []
        self.runflag = False
        self.USSIndex = 0
        self.logHandle = logger.Logger("log.log",logging.WARNING,logging.DEBUG)
    def UdpSend(self):
        ad2 = (self.IP,self.PortNum1)
        print("UDP Send USS-1\n")
        while self.runflag:
             self.udp_socket.sendto(self.CMDData,ad2)
             time.sleep(self.WAITTIME/1000)
    def Udprecv(self):
        addr = (self.ReceIP,self.PortNum2)
        receiveBuffer = 1024
        try:
            self.udp_socket.bind(addr)
            print("UDP receiver data\n")
            while self.runflag:
                #print("ce")
                try:
                    recv_data = self.udp_socket.recv(receiveBuffer)
                    self.originData.append(recv_data.decode("utf-8").split(","))
                except:
                    pass
                    #print("Annaly Error:",recv_data)
                #print("recv_data >>",recv_data)
                    pass
            #time.sleep(self.WAITTIME/1000)
        except:
            self.logHandle.error("IP地址错误")
        print("UDP stop receiver data\n")
    def closeUdpHandle(self):
        self.runflag = False
        time.sleep(1)
        self.udp_socket.close()
    def UDPReceiveMain(self):
        print("Start Process!")
        self.runflag = True
        t1 = threading.Thread(target=self.Udprecv)
        t2 = threading.Thread(target=self.UdpSend)
        t1.start()
        #t2.start()
if __name__ == "__main__":
    ethTest = UDPReceive("127.0.0.1",11204,"127.0.0.1",11205)
    ethTest.UDPReceiveMain()

