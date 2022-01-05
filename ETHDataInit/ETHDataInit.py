import os
import serial
import sys
import time

reset0 = "cd ..\r\n"

enterConfig = "cd /svp/etc\r\n"
enterUdptest = "cd /svp/bin\r\n"
configCMD ="cp -rvf /sd/config.conf /svp/etc\r\n"
slmCMD = "cp -rvf /sd/slm-config-all.xml /svp/etc\r\n"
udptestCMD = "cp -rvf /sd/svp.svc.udptest /svp/bin\r\n"

def writefile(filename,data):
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def backpack(ser):
    for i in range(2):
        ser.write(chr(0x3).encode())
        time.sleep(0.5)
    for i in range(5):
        ser.write(reset0.encode())
        time.sleep(0.5)
def sync(ser):
    for i in  range(3):
        ser.write("sync\r\n".encode())
        time.sleep(0.5)
def serialConnect(portnum):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    backpack(ser)
    return ser
def copyFileInit(ser):
    ser.write(configCMD.encode())
    time.sleep(0.5)
    sync(ser)
##    ser.write(slmCMD.encode())
##    time.sleep(0.5)
##    sync(ser)
##    ser.write(udptestCMD.encode())
##    time.sleep(0.5)
##    sync()
port = "4"
#final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
portnum = "COM"+port
ser = serialConnect(portnum)
copyFileInit(ser)
##if not os.path.exists(final_directory):
##    os.makedirs(final_directory)
##timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
##pathfile = final_directory+"\\timestamp_" +timename+".txt"
##resultlogfile = final_directory+"\\resultlog.txt"
##rece = StartupTime(pathfile,portnum)
##
##writefile(resultlogfile,"#####"*10+"StartupTime"+"####"*10+"\r\nTestTime:"+timename+">>>> "+SendData+"\r\n")
