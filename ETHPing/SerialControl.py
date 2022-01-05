import serial
import ReadConfig
import time

class SerialControl(object):
       CMDFALLBACK = "cd .."
       def __init__(self):
              readConfig = ReadConfig.ReadConfig()
              self.portNum = "COM"+readConfig.comNum
              self.connect()
       def fallBack(self):
              for i in range(3):
                     self.serialWrite(self.CMDFALLBACK)
                     time.sleep(0.5)
              for i in range(3):
                     self.serHandle.write(chr(0x3).encode())
                     time.sleep(0.5)
       def serialWrite(self,writeData):
              writeData = writeData+"\r\n"
              self.serHandle.write(writeData.encode())
       def connect(self):
             self.serHandle=serial.Serial(self.portNum)
             self.serHandle.baudrate=115200
             self.serHandle.timeout=5
             self.fallBack()
       def serialReadLine(self):
              receivedata=self.serHandle.readline()
              try:
                     receivedata = bytes(receivedata).decode('ascii')
              except:
                     receivedata = ""
              return receivedata
       def stopConnect(self):
              self.fallBack()
              self.serHandle.close()
if __name__ == "__main__":
       serialControl = SerialControl()
       while True:
              receiveData = serialControl.serialReadLine()
              print("receiveData >> ",receiveData)
