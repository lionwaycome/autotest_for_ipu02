from ctypes import *
from enum import Enum
class AutoBoxMsgType (Enum):
            E_AUTOBOX_MSG_TYPE_START = 0
            E_APA_RESP_BOX = 1
            E_HPPSER_RESP_MAPPING_BOX = 2
            E_HPPSER_RESP_PER_VEH_BOX = 3
            E_HPPSER_RESP_LOCA_BOX = 4
            E_HPPSER_RESP_MAPINFO_BOX = 5
            E_HPPSER_RESP_FREESPACE_BOX = 6
            E_CTRLALG_IN_FROM_MCU_BOX = 7
            E_CTRLALG_OUT_FROM_MCU_BOX = 8
            E_CTRLALG_MAP_FROM_MCU_BOX = 9
            E_IMU_FROM_MCU_BOX = 10
            E_CTRLALG_OUT_FROM_BOX_2MCU = 11
            E_AVM_FREESPACE_BOX = 12
            E_AVM_PD_BOX = 13
            E_USS_DATA_BOX = 14
            E_TJP_DATA_BOX = 15
            E_VEHICLE_DATA_BOX = 16
            E_ULTRASONIC_DATA_BOX = 17
            E_RPP_RESP_BOX = 18
            E_HPP_APA_RESP_BOX = 19
            E_AVM_OD_BOX = 20
            E_AVM_APBSD_BOX = 21
            E_PEB_BOX = 22
            E_USS_DATA_BIG_MAP_BOX = 23
            E_AIP_DATA = 24
            E_AUTOBOX_MSG_TYPE_MAX =25
class MsgHead(Structure):
    _fields_ = [("TagIndex",c_ubyte),\
                ("TagCount",c_ubyte),\
                ("TagLen",c_ushort),\
                ("TagVesion",c_ubyte*4),\
                ("msgType",c_ushort),\
                ("msgIndex",c_ushort),\
                ("msgLen",c_ushort),\
                ("MsgTypeTagCount",c_ushort),\
                ("bridgeTimestamp",c_ulonglong),\
                ("QnxSystemTimestamp",c_ulonglong)]
