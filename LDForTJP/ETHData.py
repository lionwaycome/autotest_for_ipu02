import threading
import socket
import msgHead
import ReadConfig
from ctypes import *

class EthTest(object):
    def __init__(self):
        readConfig = ReadConfig.ReadConfig()
        self.IP = "198.18.36.100"#readConfig.IPAddress
        self.PortNum = int(5008)
        self.ALLDATA = []
        self.originData = []
        self.runflag = False
        self.USSIndex = 0
    def Udprecv(self):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        localaddr = (self.IP,self.PortNum)
        udp_socket.bind(localaddr)
        print("UDP Receiver Data!")
        while self.runflag:
            recv_data = udp_socket.recvfrom(1024)
            self.originData.append(recv_data[0])
        udp_socket.close()
    def UdpDataSplicing(self):
        msghead = msgHead.MsgHead()
        infoData = b""
        rmsgIndex = 0
        rmsgType = 0
        index  = 0
        print("UDP Data Splicing!\n")
        while self.runflag:
            if len(self.originData):
                originaldata = self.originData[0]
                msgHeaddata = originaldata[0:32]
                memmove(addressof(msghead),msgHeaddata,sizeof(msgHead.MsgHead))
                if index == 0:
                    infoData = originaldata
                    rmsgType = msghead.msgType
                    rmsgIndex = msghead.msgIndex
                else:
                    if msghead.msgType == rmsgType:
                        if msghead.msgIndex - rmsgIndex == 1:
                            infoData += originaldata[32:]
                        else:
                            self.ALLDATA.append(infoData)
                            infoData = b""
                            infoData  += originaldata
                        rmsgType = msghead.msgType
                        rmsgIndex = msghead.msgIndex
                    else:
                        self.ALLDATA.append(infoData)
                        infoData = b""
                        infoData += originaldata
                        rmsgType = msghead.msgType
                        rmsgIndex = msghead.msgIndex
                index += 1
                del self.originData[0]
    def EthTextMain(self):
        #print("Start Process!")
        self.runflag = True
        t1 = threading.Thread(target=self.Udprecv)
        t2 = threading.Thread(target=self.UdpDataSplicing)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()
if __name__ == "__main__":
    ethTest = EthTest()
    ethTest.EthTextMain()
    
