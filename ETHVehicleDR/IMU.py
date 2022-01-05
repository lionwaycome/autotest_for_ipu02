from ctypes import *

class ImuData(Structure):
    _fields_ = [("timestamp",c_ulonglong),\
                ("Wx",c_float),\
                ("Wy",c_float),\
                ("Wz",c_float),\
                ("Ax",c_float),\
                ("Ay",c_float),\
                ("Az",c_float),\
                ("Alrx",c_float),\
                ("Alry",c_float),\
                ("Alrz",c_float),\
                ("Temp1",c_float),\
                ("Temp2",c_float),\
                ("IMURollingCounter",c_ubyte)]
#print(sizeof(ImuData))
