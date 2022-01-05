#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import time
import socket
import os
import sys
import ReadConfig
def detection(res):
    flag = 0
    for i in range(200,480):
        for j in range(400,420):
            Valuedata = res[i,j]
            if Valuedata[0] != 0 and Valuedata[1] != 0 and Valuedata[2] != 0:
                flag += 1
    print(flag)
    if flag >10 and flag <900:
                #print("flag:",flag)
        return True
    else:
        return False
def testOnDisplay(cap):
    stopflag = 1
    countnum = 0
    starttime = time.time()
    while (stopflag):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([-20, 100, 100])
        upper_red = np.array([13, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        slotdetection = res[200:480,400:420]
        gray_imageslot = cv2.cvtColor(slotdetection, cv2.COLOR_BGR2GRAY)
        countslot = cv2.countNonZero(gray_imageslot)
        cv2.imshow('heatmap',frame)
        cv2.imshow('res',res)
        cv2.imshow('res1',slotdetection)
        cv2.waitKey(1)
        #print("countslot",countslot)
        endtime = time.time()
        if detection(res) == True:
            return "PASS"
        if endtime-starttime > 60:
            return "FAIL"
def startTurnAngle():
    config = ReadConfig.ReadConfig()
    CAMERAID = int(config.detectionCameraNum)
    cap = cv2.VideoCapture(CAMERAID)
    reslut = testOnDisplay(cap)
    if reslut == "PASS":
        text = 'PASS'
    else:
        text = "FAIL;Track line angle is abnormal"
    cap.release()
    cv2.destroyAllWindows()
    return text

if __name__ == "__main__":
    startTurnAngle()
