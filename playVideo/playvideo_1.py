import numpy as np
import cv2 as cv
import threading
import time
import sys
import KeyBoard
import win32api
import win32con
import win32gui
from ctypes import *
import time
name_path_dict = {"HR_movie":[r"D:\TestStand_IPU02\dist\playVideo\HR_movie.mp4",-1565,219,1399,980],\
                  "INC_movie":[r"D:\TestStand_IPU02\dist\playVideo\INC_movie.mp4",-1547,219,1348,790],\
                  "VER_movie":[r"D:\TestStand_IPU02\dist\playVideo\VER_movie.mp4",-1565,219,1422,677],\
                  "CUR_movie":[r"D:\TestStand_IPU02\dist\playVideo\CUR_movie.mp4",-1565,219,1303,942]}
class PlayVideo(object):
    def __init__(self,videopath,x,y,Wight,Height):

        self.videopath = videopath

        self.stopflag = False
        self.x = x
        self.y = y
        self.Height = Height
        self.Wight = Wight
        
    def playvideo(self):
        cap = cv.VideoCapture(self.videopath)
        flag = 0
        cv.namedWindow("frame",0)
        cv.resizeWindow("frame",self.Wight,self.Height)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            cv.imshow('frame', frame)
            cv.waitKey(30)
            x,y,w,h = cv.getWindowImageRect('frame')
            #print(x,y,w,h)
            cv.moveWindow("frame",self.x-8,self.y-31)
            if self.stopflag:
                break
        cap.release()
        cv.destroyAllWindows()
def StartPlayVideo(videoPath,x,y,w,h):
    playvideo1 = PlayVideo(videoPath,x,y,w,h)
    playvideo1.playvideo()
#name = sys.stdin.readline()
name = "CUR_movie\n"
name = name.replace("\n","")
videoPath,x,y,w,h = name_path_dict[name]
StartPlayVideo(videoPath,x,y,w,h)





    
