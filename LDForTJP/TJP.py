#! /usr/env python

# -- coding:utf-8 --

# Date: 2021/8/19 19:58

# Author: Feng Manyi

# PyFile: TJP.py

from ctypes import *
class AppTjpResponse(Structure):
	_fields_ = [("effective_L",c_int),\
		("effective_R",c_int),\
		("theta_L",c_float),\
		("theta_R",c_float),\
		("dist_L",c_float),\
		("dist_R",c_float),\
		("confidence_L",c_float),\
		("confidence_R",c_float),\
		("curvature_L",c_float),\
		("curvature_R",c_float),\
		("lineWidth_L",c_float),\
		("lineWidth_R",c_float),\
		("lineColor_L",c_int),\
		("lineColor_R",c_int),\
		("lineType_L",c_int),\
		("lineType_R",c_int)]
class TjpDataCollect(Structure):
	_fields_ = [("fChangeLane",c_short),\
		("AbsoluteDeltaX",c_uint),\
		("AbsoluteDeltaY",c_uint),\
		("AbsoluteDeltaAngle",c_ushort),\
		("UartCount",c_ushort),\
		("ullCameraFrameNo",c_ulonglong),\
		("ulAlgStartTime",c_uint),\
		("ulAlgEndTime",c_uint),\
		("tjpFrameNo",c_uint)]
class AppTjpResponseEx(Structure):
	_fields_ = [("appTjpResponse",AppTjpResponse),\
		("tjpDataTest",TjpDataCollect)]
#print(sizeof(AppTjpResponseEx))
