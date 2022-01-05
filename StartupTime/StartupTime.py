import os
import serial
import sys
import time

reset0 = "cd ..\r\n"
reset1 ="cat /tmp/timestamp.log\r\n" 
def writefile(filename,data):
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def StartupTime(filename,portnum = "COM2"):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
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
    ser.write(reset1.encode())
    starttime = time.time()
    name_time = {}
    while True:
        receive=ser.readline()
        receivedata = str(receive,encoding="utf-8")
        if "TIMESTAMP" in receivedata:
                data = receivedata[12:].split(")")
                name_time[data[0].strip()] = float(receivedata.split("at ")[1].split(" ")[0])
                writefile(filename,receivedata+"\n")
        endtime = time.time()
        if endtime-starttime>7:
            return name_time
def startUoTimeTest():
    port = "4"
    final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
    portnum = "COM"+port
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    pathfile = final_directory+"\\timestamp_" +timename+".txt"
    resultlogfile = final_directory+"\\result.txt"
    rece = StartupTime(pathfile,portnum)
    SendData = ""
    try:
            if rece["hmi show"]  < 7:
                HMIFlag = True
            else:
                HMIFlag = False
            SendData = "HMI time:"+str(rece["hmi show"]) + "."
    except:
            HMIFlag = False
            SendData = "/tmp/timestamp.log no HMI time."
    try:
            if rece["camera show"]  < 7:
                cameraFlag = True
            else:
                cameraFlag = False
            SendData  += "video time:"+str(rece["camera show"])
    except:
            SendData  += "/tmp/timestamp.log no video time."
            cameraFlag = False
    if HMIFlag and cameraFlag:
            SendData = "PASS" 
    else:
            SendData = "FAIL;" + SendData
    writefile(resultlogfile,"#####"*10+"StartupTime"+"####"*10+"\r\nTestTime:"+timename+">>>> "+SendData+"\r\n")
    return SendData
if __name__ == "__main__":
    result = startUoTimeTest()
    print(result)
