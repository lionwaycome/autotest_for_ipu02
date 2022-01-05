import os
import time
import serial
import sys
import frameResult

reset0 = "cd /\r\n"#
reset1 = "cd /svp/etc \r\n"#
reset2 = "top\r\n" #
reset3 = ". appdbg.sh apa3\r\n"#
reset4 = ". appdbg.sh apa1\r\n" #
reset5 = "cat /storage/stdout.log\r\n"#


def writefile(filename,data):
    #print("path:",filename)
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def backboot(ser):
    ser.write(reset0.encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
def avmcap(filename,portnum="COM4"):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    #print("suce")
    #
    backboot(ser)
    time.sleep(0.5)
    ser.write(reset1.encode())#
    ser.write(reset4.encode())#
    time.sleep(0.5)
    ser.write(reset4.encode())
    time.sleep(2)
    ser.write(reset3.encode())#
    time.sleep(1.5)
    ser.write(reset0.encode())#
    time.sleep(10)
    starttime = time.time()
    ser.write(reset5.encode())#
    time.sleep(0.05)
    result = ["block"]
    while True:
        receive=ser.readline()
        receivedata = str(receive)
        #print(receivedata)
        if "APA <<  Check  Left  FPS"in receivedata or "APA <<  Check Right FPS" in receivedata:
            writefile(filename,receivedata)
            result.append(receivedata.split("FPS ")[1].split(" ")[0][:-1])
            
            print("APA << DetectionTask Check Left/Right FPS >>",receivedata.split("FPS ")[1].split(" ")[0][:-1])
        endtime = time.time()
        if endtime - starttime >60:#
            backboot(ser)
            time.sleep(0.5)
            ser.write(reset1.encode())#
            time.sleep(0.5)
            ser.write(reset4.encode())#
            return result
def startAVMCAP():
    port = "4"#sys.stdin.read()
    final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
    #final_directory = os.path.abspath('.')+"\\logdata"
    portnum = "COM"+port
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    pathfile = final_directory+"\\avmcap_" +timename+".txt"
    result = avmcap(pathfile,portnum)
    rece = result[-1]
    if len(result) < 2:
        testtoalre = "BLOCK;No found"
    else:
        testtoalre = frameResult.frameResult(result[1:],14,10,14)#"PASS;APA << DetectionTask Check Left/Right FPS all > 15"
    resultfile = final_directory+"\\result.txt"
    writefile(resultfile,"AVMCAPSresult:"+testtoalre+"\n")
    return testtoalre
if __name__ == "__main__":
    result = startAVMCAP()
    print(result)








    
