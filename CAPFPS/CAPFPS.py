import os
import time
import serial
import socket
import sys
import frameResult

reset0 = "cd /\r\n"###
reset1 = "cat /storage/stdout.log\r\n"
reset7 = "cd /storage\r\n"#
reset8 = "cp -rf stdout.log /sd/tracelog/\r\n"#
'''

'''
def writefile(filename,data):
    #print("path:",filename)
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def backboot(ser):
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    ser.write(reset0.encode())
    time.sleep(0.5)
    ser.write(reset0.encode())
    time.sleep(0.5)
    ser.write(reset0.encode())
    time.sleep(0.5)
    ser.write(reset0.encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
def CAPFPSGTest(filename,portnum="COM4"):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    #####
    backboot(ser)
    starttime = time.time()
    result = ["block"]
    time.sleep(1)
    ser.write(reset1.encode())
    time.sleep(0.05)
    while True:
        receive=ser.readline()
        receivedata = str(receive)
        writefile(filename,receivedata)
        if "CAP ...   FPSG =" in receivedata:
            try:
                result.append(receivedata.split()[4][0:5])
            except: 
                pass
        endtime = time.time()
        if endtime - starttime >80:
            backboot(ser)
            return result
def startCAPFPS():
    port = "4" #= sys.stdin.read()
    final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
    #final_directory = os.path.abspath('.')+"\\logdata"
    portnum = "COM"+port
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    pathfile = final_directory+"\\CAPFPSG_" +timename+".txt"
    result = CAPFPSGTest(pathfile,portnum)
    rece = result[-1]
    testtoalre = frameResult.frameResult(result[1:],24,20,24)#"PASS;CAP FPSG:"+rece
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    ser.write(reset0.encode())
    time.sleep(0.5)
    ser.write(reset7.encode())
    #print("reset7:",reset7)
    time.sleep(0.5)
    ser.write(reset8.encode())
    #print("reset8:",reset8)
    #time.sleep(10)
    pscpCMD = "D:\\UDP_Autolibrary_Project\\Python\\pscp.exe -pw root root@198.18.36.96:"
    path2 = " D:\\UDP_Autolibrary_Project\\Python\\logdata"
    path3 = "/sd/tracelog/stdout.log"
##    try:
##        a = os.system(command = pscpCMD+path3+path2)
##        time.sleep(10)       
##    except:
##        pass
        #print(a)
    resultfile = final_directory+"\\result.txt"
    writefile(resultfile,"CAPFPSresult:"+testtoalre+"\n")
    return testtoalre
if __name__ == "__main__":
    result = startCAPFPS()
    print(result)
