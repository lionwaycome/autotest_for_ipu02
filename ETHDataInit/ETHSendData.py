import os
import serial
import sys
import time

udptestCMD = "/svp/bin/svp.svc.udptest & \r\n"
reset0 = "cd .. \r\n"

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
def udptestInit():
    portnum = "COM4"
    ser = serialConnect(portnum)
    ser.write(udptestCMD.encode())
    time.sleep(0.5)
    sync(ser)
if __name__ == "__main__":
    udptestInit()

