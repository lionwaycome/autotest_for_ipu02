#coding=utf-8

import sys


def readVersion():
    F_VERSION = open("D:\\01_TTD\\TestStand_Test\\G7PH\Version1.txt")
    line = F_VERSION.readline()
    SWVersion=line.split(':',1)
    Version = SWVersion[1]

    #F_VERSION.write("HWVersion:B1.112.2")
    print(Version)

    
    #F_VERSION.close()


if __name__=="__main__":
    readVersion()
