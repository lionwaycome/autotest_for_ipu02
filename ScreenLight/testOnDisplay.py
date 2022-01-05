#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import time
import socket
import os
import sys
import serial
import ReadConfig
final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
reset0 = "cd ..\r\n"

def writefile(filename,data):
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def detection(res):
    for i in range(0,480):
        for j in range(0,640):
            Valuedata = res[i,j]
            if Valuedata[0] != 0 and Valuedata[1] != 0 and Valuedata[2] != 0:
                return True
    return False
def testOnDisplay(cap,pathfile):
    stopflag = 1
    countnum = 0
    starttime = time.time()
    fps = 15
    sucnum = 0
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    #videoWriter = cv2.VideoWriter(final_directory+'\\testOndisplayvideo.mp4', cv2.VideoWriter_fourcc('M','P','4','V'), fps, size)
    while (stopflag):
        ret, frame = cap.read()
        #videoWriter.write(frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([-20, 100, 100])
        upper_red = np.array([13, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        gray_imageslot = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        countSlot = cv2.countNonZero(gray_imageslot)
        cv2.imshow('heatmap',frame)
        cv2.imshow('res',res)
        cv2.waitKey(1)
        endtime = time.time()
        print("countSlot:",countSlot)
        writefile(pathfile,str("counSlot>> ")+str(countSlot)+"\n")
        if countSlot > 100:
                sucnum += 1
        else:
                sucnum = 0
        if sucnum > 20:
                result = "PASS"
                break
        if endtime-starttime > 120:
            result = "FAIL"
            break
    cap.release()
    cv2.destroyAllWindows()
    return result
def backpack(ser):
    for i in range(2):
        ser.write(chr(0x3).encode())
        time.sleep(0.5)
    for i in range(5):
        ser.write(reset0.encode())
        time.sleep(0.5)
def enterparking():
    
    reset3 = ". appdbg.sh apa3\r\n"#####
    
    reset4 = ". appdbg.sh apa1\r\n" ####
    
    ser=serial.Serial("COM4")
    
    ser.baudrate=115200
    
    ser.timeout=5

    backpack(ser)
    
    ser.write(reset4.encode())
    
    time.sleep(0.5)
    
    ser.write(reset4.encode())
    
    time.sleep(1)
    
    ser.write(reset3.encode())
    
    time.sleep(5)
    
    ser.write(reset4.encode())
    
    ser.close()

def testMain():    
    result =""
    enterparking()
    time.sleep(1)
    pathfile = final_directory+"/testOndisplay.txt"
    config = ReadConfig.ReadConfig()
    camernum = int(config.detectionCameraNum)
    cap = cv2.VideoCapture(camernum)
    reslut = testOnDisplay(cap,pathfile)
    if reslut == "PASS":
        text = 'PASS'
    else:
        text = "FAIL;The display doesn't light up"
    writefile(pathfile,"\n******"*10+"TestResult"+"******"*10+"\n")
    writefile(pathfile,text)
    #print(text)
    return text
if __name__ == "__main__":
    testMain()
##    sys.stdout.write(text)
##    sys.stdout.write(text)

