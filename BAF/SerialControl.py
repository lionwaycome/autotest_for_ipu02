import serial
import ReadConfig
import time

class SerialControl(object):
       CMDFALLBACK = "cd .."
       def __init__(self):
              readConfig = ReadConfig.ReadConfig()
              self.portNum = "COM4"#+readConfig.comNum
              self.connect()
              #self.fallBack()
       def fallBack(self):
              for i in range(3):
                     self.serHandle.write((self.CMDFALLBACK+"\r\n").encode())
                     time.sleep(0.5)
              for i in range(3):
                     self.serHandle.write(chr(0x3).encode())
                     time.sleep(0.5)
       def serialWrite(self,writeData):
              self.fallBack()
              writeData = writeData+"\r\n"
              self.serHandle.write(writeData.encode())
       def connect(self):
             self.serHandle=serial.Serial(self.portNum)
             self.serHandle.baudrate=115200
             self.serHandle.timeout=5
             #self.fallBack()
       def serialReadLine(self):
              receivedata=self.serHandle.readline()
              try:
                     receivedata = bytes(receivedata).decode('ascii')
              except:
                     receivedata = ""
              return receivedata
       def stopConnect(self):
              self.serHandle.close()
if __name__ == "__main__":
       serialControl = SerialControl()
       serialControl.serialWrite("cat /storage/stdout.log")
       while True:
              receiveData = serialControl.serialReadLine()
              print("receiveData >> ",receiveData)
