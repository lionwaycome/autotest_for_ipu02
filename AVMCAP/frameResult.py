import numpy as np


def continResult(data,value):
    
    flag = 0
    for itemdata in data:
        if itemdata < value:
            flag += 1
        else:
            flag = 0
        if flag >= 10:
            return False
    return True

def frameResult(strframedata,meanvalue,minvalue,continvalue):
    framedata = []
    allResult = ""
    for item in strframedata[1:]:
        try:
            framedata.append(float(item))
        except:
            pass
    rmeanvalue = np.mean(framedata)
    meanreturn = "meanValue:"+str(rmeanvalue)
    if rmeanvalue >= meanvalue:
        meanre = True
    else:
        meanre = False 
    rminvalue = np.min(framedata)
    rcontine = continResult(framedata,continvalue)
    if rcontine:
        continereturn = ".There is no 10 frames in a row low than "+str(continvalue)
    else:
        continereturn = ".There is 10 frames in a row low than "+str(continvalue)
    if rminvalue >= minvalue:
        minre = True
        minvaluereturn = ".Whole is greater than the " + str(minvalue)
    else:
        minre = False
        minvaluereturn = ".Some values are " + str(rminvalue)
    if meanre and rcontine and minre:
        return"PASS"#+meanreturn+continereturn+minvaluereturn
    else:
        return"FAIL;"+meanreturn+continereturn+minvaluereturn

if __name__ == "__main__":
    print(frameResult([1,2,3,4,15,6,7,8,9,1,2,21,21],10,4,10))
    #frameResult()