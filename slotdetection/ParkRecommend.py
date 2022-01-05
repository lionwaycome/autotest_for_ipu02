#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import time
import os
import sys
import numpy as np
import threading
import sys
import WriteLog
import ReadConfig

LOWERCOLOR = np.array([30, 40, 45])#np.array([55, 50, 46])

UPPERCOLOR = np.array([77, 255, 255])#np.array([77, 255, 255]) #green

config = ReadConfig.ReadConfig()

CAMERNUM = int(config.detectionCameraNum)

SLOTDETECTIONTIME = 60

def ParkingRecommend():
    countnum = 0
    starttime = time.time()
    sucnum = 0
    #testresult = "FAIL"
    cap = cv2.VideoCapture(CAMERNUM)
    while (1):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWERCOLOR, UPPERCOLOR)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        slotdetection = res[230:400,200:270]
        #slotdetection1 = frame[270:365,155:195]
        gray_imageslot = cv2.cvtColor(slotdetection, cv2.COLOR_BGR2GRAY)
        cv2.imshow("ParkRecom1",frame)
        cv2.imshow('ParkRecom12', slotdetection)
        cv2.waitKey(1)
        endtime = time.time()
        countslot = cv2.countNonZero(gray_imageslot)
        #print("countslot >> ",countslot)
        if countslot > 100:
            sucnum += 1
        else:
            sucnum = 0
        if endtime - starttime > SLOTDETECTIONTIME:
            testresult = "FAIL"
            break
        if sucnum > 20:
            testresult = "PASS"
            break
    cap.release()
    cv2.destroyAllWindows()
    #print(testresult)
    sys.stdout.write(testresult)
    WriteLog.writefile("Parking",testresult)
if __name__ == "__main__":
    #StartDetection(r"D:\DEQTV\2021\06\IPU02\SmokeTest\Src\ParkingSlot\SlotDetection\movie.avi")
    ParkingRecommend()
