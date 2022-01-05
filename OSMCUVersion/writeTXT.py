#coding=utf-8

import sys

def WriteTXT(Version):
    F_VERSION = open("D:\\TestStand_IPU02\\Version.txt","w")

    F_VERSION.write("Software Version:"+Version)

if __name__=="__main__":
    WriteTXT("SOC:222.22.1;mcu:ss.2.3")
