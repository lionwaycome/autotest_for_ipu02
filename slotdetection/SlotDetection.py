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

LOWERCOLOR = np.array([30, 43, 46])

UPPERCOLOR = np.array([34, 255, 255])
config = ReadConfig.ReadConfig()

CAMERNUM = int(config.detectionCameraNum)

SLOTDETECTIONTIME = 60

def slotdetection():
    countnum = 0
    starttime = time.time()
    sucnum = 0
    testresult = "FAIL"
    #print("Camera Start.")
    cap = cv2.VideoCapture(CAMERNUM)
    #print("Camera Start.")
    while (1):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWERCOLOR, UPPERCOLOR)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        #slotdetection = res[200:400,200:270]
        slotdetection = res[200:400,80:270]
        gray_imageslot = cv2.cvtColor(slotdetection, cv2.COLOR_BGR2GRAY)
        cv2.imshow("cam",frame)
        cv2.imshow('Slot', slotdetection)
        #cv2.imshow("Slot1",slotdetection1)
        cv2.waitKey(1)
        endtime = time.time()
        countslot = cv2.countNonZero(gray_imageslot)
        #print("countslot >> ",countslot)
        if countslot > 50:
            sucnum += 1
        else:
            sucnum = 0
        if endtime - starttime > SLOTDETECTIONTIME:
            testresult = "FAIL"
            break
        if sucnum > 20:
            testresult =  "PASS"
            break
    cap.release()
    cv2.destroyAllWindows()
    WriteLog.writefile("SlotDetection",testresult)
    sys.stdout.write(testresult)
    #return testresult
if __name__ == "__main__":
   slotdetection()
