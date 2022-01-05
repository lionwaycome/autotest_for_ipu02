#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import time
import os
import sys
import numpy as np
import sys
import ReadConfig

class CameraDetection(object):
    MAXDETECTION = 120
    TESTNUM = 20
    def __init__(self,lowerColor,upperColor,xyRange,minValue):
        self.LOWERCOLOR = np.array(lowerColor)
        self.UPPERCOLOR = np.array(upperColor)
        readConfig = ReadConfig.ReadConfig()
        self.CAMERNUM = 0 #int(readConfig.detectionCameraNum)
        self.xyRange = xyRange
        self.minValue = minValue
        self.openCamera()
    def openCamera(self):
        self.cap = cv2.VideoCapture(self.CAMERNUM)
    def closeCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()
    def startDetection(self):
        startTime = time.time()
        sucnum = 0
        testResult = ""
        x_min,x_max,y_min,y_max = self.xyRange
        while True:
            ret,frame = self.cap.read()
            hsvframe  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            maskframe = cv2.inRange(hsvframe, self.LOWERCOLOR, self.UPPERCOLOR)
            resframe = cv2.bitwise_and(frame, frame, mask=maskframe)
            detectionframe = resframe[x_min:x_max,y_min:y_max]
            gray_imageslot = cv2.cvtColor(detectionframe, cv2.COLOR_BGR2GRAY)
            countSlot = cv2.countNonZero(gray_imageslot)
            cv2.imshow("camera",frame)
            cv2.imshow('Detection', detectionframe)
            cv2.waitKey(1)
            #print(countSlot)
            if countSlot > self.minValue:
                sucnum += 1
            else:
                sucnum = 0
            endTime = time.time()
            print("countSlot:",countSlot)
            if endTime - startTime > self.MAXDETECTION:
                testResult = "FAIL"
                break
            if sucnum > self.TESTNUM:
                testResult = "PASS"
                break
        self.closeCamera()
        return testResult
if __name__ == "__main__":
    cameraDetection = CameraDetection([0, 0, 221],[180, 30, 251],[270,365,155,195],800)
    result = cameraDetection.startDetection()
    print(result)
