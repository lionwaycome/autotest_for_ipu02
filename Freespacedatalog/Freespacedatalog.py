import os
import time
import serial
import sys
import socket

NORMORALLINNUM = 120  ### freesp
PLAYBACKNUM = 4 ####
FILENUM = 0

def writefile(filename,data):
    with open(filename,"a+") as f:
        f.write(data)
    f.close
def sendcatinfor(ser,pathname,palynum):
    """
    
    """
    writefile(pathname,"******"*10+str(palynum)+" Creatfile"+"******"*10+"\n")
    ser.write(("ls\r\n").encode())
    txtfile = []
    starttiem = time.time()
    while True:
        receive=ser.readline()
        receivedata = str(receive)
        if ".txt" in receivedata:
            txtfile.append(receivedata)
            writefile(pathname,receivedata)
        endtime = time.time()
        if (endtime - starttiem) > 10:
            break
    if len(txtfile) > FILENUM:
        return "PASS",len(txtfile)
    else:
        return "FAIL",len(txtfile)
        #print("recedata>> ",receivedata)
def frplayback(path,ser,palynum):
    reset0 = "cd ..\r\n"
    ser.write(reset0.encode())
    time.sleep(0.5)
    reset0_1 = "cd /sd/output/fs_out1\r\n"
    ser.write(reset0_1.encode())
    time.sleep(0.5)
    reset0_2 = "rm -rf *.txt\r\n"
    ser.write(reset0_2.encode())
    time.sleep(0.5)
    reset0 = "cd ..\r\n"
    ser.write(reset0.encode())
    time.sleep(0.5)
    reset = "cd /vision_apps\r\n"   #XXXXXXXXXXX
    ser.write(reset.encode())     #
    time.sleep(2)
    reset1 = "./vx_desay_all_func_playback.out --cfg /sd/app_all_func_playback_fs.cfg\r\n"
    ser.write(reset1.encode())
    starttime = time.time()
    linenum = 0
    writefile(path,"******"*10+str(palynum)+"******"*10+"\n")
    while True:
        receive=ser.readline()
        if str(receive) != "b''" :
            linenum += 1
            writefile(path,str(receive)+"\n")
            #print("linenum",linenum)
        endtime = time.time()
        if endtime-starttime>30:
            break
        #print(">>>>>>>",receive)
    
    ser.write(chr(0x3).encode())
    time.sleep(10)
    reset0 = "cd ..\r\n"
    ser.write(reset0.encode())
    time.sleep(0.5)
    reset0_1 = "cd /sd/output/fs_out1\r\n"
    ser.write(reset0_1.encode())
    time.sleep(0.5)
    s=[]
    if linenum < NORMORALLINNUM:
        return "FAIL",linenum,0
    else:
        re,filenum = sendcatinfor(ser,path,palynum)
        return re,linenum,filenum
def SendSerial(path,portnum = "COM5"):
    ser=serial.Serial(portnum)
    ser.baudrate=115200
    ser.timeout=5
    palybacknum = 0
    testResult = []
    while True:
        palybacknum += 1
        result,linenum,filenum = frplayback(path,ser,palybacknum)
        testResult.append([result,linenum,filenum])
        if result == "PASS":
            break
        if palybacknum >PLAYBACKNUM:
            break
    return testResult
def startFreespaceDataLog():
    port = "4"#sys.stdin.read()
    final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"
    # final_directory = os.path.abspath('.')+"\\logdata"
    portnum = "COM"+port
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    pathfile = final_directory+"/Freespacedatalog_" +timename+".txt"
    frplayresult = SendSerial(pathfile,portnum)
    seriallinenum = ""
    for it,item in enumerate(frplayresult):
         seriallinenum += " "+str(it+1)+"_rows:"+str(item[1])
    filenum = ""
    total1result =frplayresult[-1][0]#+";"+"Playback Numbers:"+str(len(frplayresult))+" "+seriallinenum
    writefile(pathfile,"\n******"*10+"result"+"******"*10+"\n")
    writefile(pathfile,total1result)
    return total1result
if __name__ == "__main__":
    result = startFreespaceDataLog()
    print(result)
