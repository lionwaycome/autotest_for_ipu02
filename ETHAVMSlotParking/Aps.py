from ctypes import *
class ApaTargetSlotPlaceExTest(Structure):
	_fields_ = [("ullCameraFrameNo",c_ulonglong),\
		("ulAlgStartTime",c_uint),\
		("ulAlgEndTime",c_uint),\
		("ulApsSlotInfoFrameNo",c_uint),\
		("iRecommedLable",c_int)]
class ApaTargetSlotPlace(Structure):
	_fields_ = [("apaSlotA_x",c_short),\
		("apaSlotA_y",c_short),\
		("apaSlotB_x",c_short),\
		("apaSlotB_y",c_short),\
		("apaSlotC_x",c_short),\
		("apaSlotC_y",c_short),\
		("apaSlotD_x",c_short),\
		("apaSlotD_y",c_short)]
class ApaRelocationExTest(Structure):
	_fields_ = [("ullCameraFrameNo",c_ulonglong),\
		("ulAlgStartTime",c_uint),\
		("ulAlgEndTime",c_uint),\
		("ulRelocFrameNo",c_uint),\
		("usUartCount",c_ushort)]
class ApaRelocationInfo(Structure):
	_fields_ = [("apaVerSlotLeftLine",c_ushort),\
		("apaVerSlotRightLine",c_ushort),\
		("apaVerSlotLeftLineTheta",c_float),\
		("apaVerSlotRightLineTheta",c_float),\
		("apaVerSlotDistL",c_float),\
		("apaVerSlotDistR",c_float),\
		("apaParSlotUpLine",c_ushort),\
		("apaParSlotDownLine",c_ushort),\
		("apaParSlotUpTheta",c_float),\
		("apaParSlotDownTheta",c_float),\
		("apaParSlotUpLineDist",c_float),\
		("apaParSlotDownLineDist",c_float),\
		("apaAbsoluteDeltaX",c_uint),\
		("apaAbsoluteDeltaY",c_uint),\
		("apaAbsoluteAngle",c_ushort),\
		("apaLeftResultSource",c_ushort),\
		("apaRightResultSource",c_ushort)]
class ApaRecordParkInInfo(Structure):
	_fields_ = [("update_resp",c_ubyte),\
		("MCU_ParkInOrOutFlag_InStore",c_ubyte),\
		("APA_ParkSlotType_InStore",c_ubyte),\
		("APA_ParkPlaceInfoType_InStore",c_ubyte),\
		("APA_ParkType_InStore",c_ubyte),\
		("APA_ParkBehaviorType_InStore",c_ubyte),\
		("APA_ParkDirectionInfoType_InStore",c_ubyte),\
		("APA_ParkSlot_Side_InStore",c_ubyte),\
		("APA_ParkPlaceX1_InStore",c_int),\
		("APA_ParkPlaceX2_InStore",c_int),\
		("APA_ParkPlaceX3_InStore",c_int),\
		("APA_ParkPlaceX4_InStore",c_int),\
		("APA_ParkPlaceY1_InStore",c_int),\
		("APA_ParkPlaceY2_InStore",c_int),\
		("APA_ParkPlaceY3_InStore",c_int),\
		("APA_ParkPlaceY4_InStore",c_int),\
		("HppParkingInGlobalStopPt_x_InStore",c_float),\
		("HppParkingInGlobalStopPt_y_InStore",c_float),\
		("HppParkingInGlobalStopPt_yaw_InStore",c_float),\
		("ALG_Factor1_Out_InStore",c_float),\
		("ALG_Factor2_Out_InStore",c_float),\
		("ALG_Factor3_Out_InStore",c_float),\
		("ALG_Factor1_In_InStore",c_float),\
		("ALG_Factor2_In_InStore",c_float),\
		("ALG_Factor3_In_InStore",c_float)]
class BlockInfo(Structure):
	_fields_ = [("iHaveBlock",c_ubyte),\
		("iBlockToRect",c_short),\
		("fBlockToCarDist",c_ushort),\
		("fBlockLineAngle",c_float)]
class AppApaResponse(Structure):
	_fields_ = [("apaParkMode",c_ushort),\
		("apaParkInMode",c_ushort),\
		("apaParkOutMode",c_ushort),\
		("apaStatusResp",c_ushort),\
		("apaParkModeReq",c_ushort),\
		("apaSearchStatus",c_ushort),\
		("apaParkType",c_ushort),\
		("apaParkFusionType",c_ushort),\
		("apaTargetSlot",ApaTargetSlotPlace),\
		("apaRelocInfo",ApaRelocationInfo),\
		("apaUpDownSlotSOD",c_ushort),\
		("apaWarningTone",c_ushort),\
		("apaTimeOut",c_ushort),\
		("apaRecomSwitchResp",c_ushort),\
		("apaShortestDist",c_ushort),\
		("apaTrackOrDetectSlot",c_ushort),\
		("apaMCUDebugParam",c_ushort),\
		("apaRoadEdgeDistance",c_ushort),\
		("apaBackgroundSearchResult",c_ushort),\
		("apaSceneType",c_ushort),\
		("apaNarrowSlot",c_ubyte),\
		("apaRecordParkInInfo",ApaRecordParkInInfo),\
		("apaReadyStatus",c_ubyte),\
		("apaBlockInfo",BlockInfo)]
class AppApaResponseEx(Structure):
	_fields_ = [("appApaResponse",AppApaResponse),\
		("apaTargetSlotTest",ApaTargetSlotPlaceExTest),\
		("apaRelocaTest",ApaRelocationExTest)]
class ApaParkPlace(Structure):
	_fields_ = [("apaCoordinate_X",c_short),\
		("apaCoordinate_Y",c_short),\
		("apaTheta",c_float)]
class ApaUssBandC(Structure):
	_fields_ = [("apaBPoint_X",c_short),\
		("apaBPoint_Y",c_short),\
		("apaCPoint_X",c_short),\
		("apaCPoint_Y",c_short)]
class ApaParkInInfoRecordReq(Structure):
	_fields_ = [("update_req",c_ubyte),\
		("MCU_ParkInOrOutFlag_InStore",c_ubyte),\
		("APA_ParkSlotType_InStore",c_ubyte),\
		("APA_ParkPlaceInfoType_InStore",c_ubyte),\
		("APA_ParkType_InStore",c_ubyte),\
		("APA_ParkBehaviorType_InStore",c_ubyte),\
		("APA_ParkDirectionInfoType_InStore",c_ubyte),\
		("APA_ParkSlot_Side_InStore",c_ubyte),\
		("APA_ParkPlaceX1_InStore",c_int),\
		("APA_ParkPlaceX2_InStore",c_int),\
		("APA_ParkPlaceX3_InStore",c_int),\
		("APA_ParkPlaceX4_InStore",c_int),\
		("APA_ParkPlaceY1_InStore",c_int),\
		("APA_ParkPlaceY2_InStore",c_int),\
		("APA_ParkPlaceY3_InStore",c_int),\
		("APA_ParkPlaceY4_InStore",c_int),\
		("HppParkingInGlobalStopPt_x_InStore",c_float),\
		("HppParkingInGlobalStopPt_y_InStore",c_float),\
		("HppParkingInGlobalStopPt_yaw_InStore",c_float),\
		("ALG_Factor1_Out_InStore",c_float),\
		("ALG_Factor2_Out_InStore",c_float),\
		("ALG_Factor3_Out_InStore",c_float),\
		("ALG_Factor1_In_InStore",c_float),\
		("ALG_Factor2_In_InStore",c_float),\
		("ALG_Factor3_In_InStore",c_float)]
class MCUApaRequest(Structure):
	_fields_ = [("apaParkMode",c_ushort),\
		("apaParkInMode",c_ushort),\
		("apaParkOutMode",c_ushort),\
		("apaRecomSwitch",c_ushort),\
		("apaParkInDirection",c_ushort),\
		("apaDefaultParkModeReq",c_ushort),\
		("apaSlotInfoReq",c_ushort),\
		("apaStatusReq",c_ushort),\
		("apaParkModeReq",c_ushort),\
		("apaHandshakeStatus",c_ushort),\
		("apaPredictedSlot",ApaParkPlace),\
		("apaTargetSlot",ApaParkPlace),\
		("apaRelocationStatus",c_ushort),\
		("apaUpdateUssSlot",ApaUssBandC),\
		("apaForwardMileage",c_short),\
		("apaBackwardMileage",c_short),\
		("apaParkInInfoRecordReq",ApaParkInInfoRecordReq),\
		("RPP_ilabel",c_uint)]
