import socket
import time
import readCSVFile
import threading

class USSUdpSend(object):
    def __init__(self):
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.ad2 = ("127.0.0.1",11205)
            self.flag = False
    def threadSearchSpace(self):
        self.flag = False
        time.sleep(0.5)
        self.flag = True
        t1 = threading.Thread(target = self.SearchSpace)
        t1.start()
    def threadObstacles(self):
        self.flag = False
        time.sleep(0.5)
        self.flag = True
        t1 = threading.Thread(target = self.sendObstacles)
        t1.start()
    def threadDefault(self):
        self.flag = False
        time.sleep(0.5)
        self.flag = True
        t1 = threading.Thread(target = self.sendDefaultValue)
        t1.start()
    def SearchSpace(self):
        ussData = readCSVFile.readCSV(r"D:\TestStand_IPU02\dist\USSFPGA\data\USS.CSV")
        for itemdata in ussData[3:]:
               sendData =""
               for uss in itemdata[1:]:
                      if uss == "2.5" or uss == "5":
                             sendData += "0,"
                      else:
                             sendData += str(float(uss)/170)+","
               sendData = sendData[:-1]
               #print(sendData)
               self.udp_socket.sendto(sendData.encode("utf-8"),self.ad2)
               time.sleep(0.02)
               if not self.flag:
                    break
    def sendObstacles(self):
        while self.flag:
            sendData = str(float(1)/170)+","+str(float(1)/170)+","+\
                     str(float(1)/170)+","+str(float(1)/170)+","+\
                     str(float(1)/170)+","+str(float(1)/170)+","+\
                     str(float(1)/170)+","+str(float(1)/170)+","+\
                     str(float(1)/170)+","+str(float(1)/170)+","+\
                     str(float(1)/170)+","+str(float(1)/170)
            self.udp_socket.sendto(sendData.encode("utf-8"),self.ad2)
            time.sleep(0.01)
    def sendDefaultValue(self):
        while self.flag:
            sendData = "0,0,0,0,0,"+str(float(0)/170)+",0,0,0,0,0,0"
            self.udp_socket.sendto(sendData.encode("utf-8"),self.ad2)
            time.sleep(0.01)
    def close(self):
        self.flag = False
        self.udp_socket.close()
if __name__ == "__main__":
 ussUdpSend = USSUdpSend()
 ussUdpSend.threadDefault()
