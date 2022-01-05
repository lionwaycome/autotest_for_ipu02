import os
import time
import serial
import sys

port = "4"#sys.stdin.read()
final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
reset0 = "cd /\r\n"###
reset1 ="top\r\n" #CPU
reset2 = "cd /svp/etc \r\n"
reset3 = ". appdbg.sh apa3\r\n"#####
reset4 = ". appdbg.sh apa1\r\n" ####
reset5 = "tracelogger -s 5 -f /dev/shmem/tracelog_"
reset6 = "cp -rf /dev/shmem/tracelog_"
reset7 = "cd /storage\r\n"#
reset8 = "cp -rf stdout.log /sd/tracelog"#
portnum = "COM"+port
if not os.path.exists(final_directory):
    os.makedirs(final_directory)
    
timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
pathfile = final_directory+"\\ApaCPUusage_" +timename+".txt"
reset5 += timename+".kev\r\n"
reset6 += timename+".kev /sd/tracelog/\r\n"

pscpCMD = "D:\\UDP_Autolibrary_Project\\Python\\pscp.exe -pw root root@198.18.36.96:"
path1 = "/sd/tracelog/tracelog_"+timename+".kev "
path2 = final_directory
path3 = "/sd/tracelog/stdout.log "
waittime = 600
def writefile(filename,data):
    #print("path:",filename)
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def backboot(ser):
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
def parkingTest(filename,portnum="COM5"):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    #####
    backboot(ser)
    time.sleep(0.5)
    ser.write(reset2.encode())
    ser.write(reset4.encode())
    time.sleep(0.5)
    ser.write(reset4.encode())
    time.sleep(2)
    ser.write(reset3.encode())
    time.sleep(1.5)
    ####
    ser.write(reset1.encode())
    time.sleep(0.5)
    starttime = time.time()
    result = []
    while True:
        receive=ser.readline()
        #print(receive)
        endtime = time.time()
        writefile(filename,str(receive)+"\n")
        if "CPU 0 idle:" in str(receive):
            #writefile(filename,str(receive)+"\n")
            #for s in str(receive).split():
            value = str(receive).split()[5]
            p_value = int(value.split("%")[0])
            result.append(p_value)
        if result != []:
            if "CPU 1 idle:" in str(receive):
                #writefile(filename,str(receive)+"\n")
                value1 = str(receive).split()[5]
                p_value1 = int(value1.split("%")[0])
                #print("p_value1:",p_value1)
                result.append(p_value1)
                break
        if endtime-starttime>10:
            result.append(-1)
            result.append(-1)
            break
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    #print(result)
    time.sleep(waittime)#######
    ser.write(reset1.encode())
    time.sleep(0.5)
    starttime = time.time()
    while True:
        receive=ser.readline()
        #print(receive)
        endtime = time.time()
        writefile(filename,str(receive)+"\n")
        if "CPU 0 idle:" in str(receive):
            #writefile(filename,str(receive)+"\n")
            #for s in str(receive).split():
            value = str(receive).split()[5]
            p_value = int(value.split("%")[0])
            result.append(p_value)
        if result != []:
            if "CPU 1 idle:" in str(receive):
                #writefile(filename,str(receive)+"\n")
                value1 = str(receive).split()[5]
                p_value1 = int(value1.split("%")[0])
                #print("p_value1:",p_value1)
                result.append(p_value1)
                break
        if endtime-starttime>10:
            result.append(-1)
            result.append(-1)
            break
    ser.write(chr(0x3).encode())
    time.sleep(0.5)
    ser.write(chr(0x3).encode())
    ser.write(reset2.encode())
    time.sleep(0.5)
    ser.write(reset4.encode())
    time.sleep(0.5)
    ser.write(reset5.encode())
    #print("reset5:",reset5)
    time.sleep(10)
    ser.write(reset6.encode())
    #print("reset6:",reset6)
    time.sleep(10)
    ser.write(reset0.encode())
    time.sleep(1)
    return result
def startTest():
    rece = parkingTest(pathfile,portnum)
    #print("rece>>",rece)
    testtoalre = "PASS"
    res = ""
    if (rece[0] != -1) and (rece[1] != -1):
        print(rece[0]+rece[1])
        if rece[0]+rece[1] < 40:
            print(rece[0]+rece[1])
            testtoalre = "FAIL;"
            res += "StartInput:"+str(rece[0]+rece[1])+"% "
    else:
        res += "StartInput:block "
    if rece[2] != -1 and rece[3] != -1:
        print(rece[2]+rece[3])
        if rece[2]+rece[3] < 40:
            
            testtoalre = "FAIL;"
            res += "10min:"+str(rece[2]+rece[3])+"%"
    else:
        res += "10min:block "
    testtoalre += res
    try:
        a = os.system(command = pscpCMD+path1+path2)
        time.sleep(10)       
    except:
        pass 
        #print(a)
    #sys.stdout.write(testtoalre)
    return testtoalre
if __name__ == "__main__":
    result = startTest()
    print(result)
