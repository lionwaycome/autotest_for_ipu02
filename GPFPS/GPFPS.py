import os
import time
import serial
import socket
import sys
import frameResult

reset0 = "cd /\r\n"###
reset1 = "cat /storage/stdout.log\r\n"
'''

'''
def writefile(filename,data):
    #print("path:",filename)
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def backboot(ser):
    for index in range(6):
        ser.write(chr(0x3).encode())
        time.sleep(0.5)
def GPFPSGTest(filename,portnum="COM5"):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    #####
    backboot(ser)
    starttime = time.time()
    result = ["block"]
    ser.write(reset1.encode())
    time.sleep(0.01)
    while True:
        receive=ser.readline()
        receivedata = str(receive)
##        try:
##            receivedata = str(receive,encoding="utf-8")
##        except:
##            receivedata = ""
        writefile(filename,receivedata+"\n")
        if " GP FPSG = " in receivedata:
            try:
                timestamp = int(receivedata.split()[-1].split("(")[0])
            except:
                timestamp = 0;
            if timestamp > 60:
                print("timestamp",timestamp,"GP FPSG",receivedata.split()[-6])
                writefile(filename,receivedata+"\n")
                result.append(receivedata.split()[-6])
            #print("GP FPS >>",receivedata.split()[-1])
            #return result
        endtime = time.time()
        if endtime - starttime >70:
            #result = 'block'
            backboot(ser)
            return result
def startGPFPS():
    port = "4"#sys.stdin.read()
    final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
    #final_directory = os.path.abspath('.')+"\\logdata"#os.path.join(current_directory, r'/logdata')
    portnum = "COM"+port
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    pathfile = final_directory+"\\GPFPSG_" +timename+".txt"
    result = GPFPSGTest(pathfile,portnum)
    rece = result[-1]
    testtoalre = frameResult.frameResult(result[1:],20,18,20)#"PASS;GP fps:"+rece
    resultfile = final_directory+"\\result.txt"
    writefile(resultfile,"GPFPSresult:"+testtoalre+"\n")
    return testtoalre
if __name__ == "__main__":
    result = startGPFPS()
    print(result)
