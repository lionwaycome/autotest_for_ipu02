@echo off
cd D:\TestStand_IPU02\dist\USBRelay\
echo wscript.sleep 100>sleep.vbs
CommandApp_USBRelay 6QMBS open 01
start /wait sleep.vbs
CommandApp_USBRelay 6QMBS close 02
start /wait sleep.vbs
CommandApp_USBRelay 6QMBS close 03
start /wait sleep.vbs
echo wscript.sleep 10000>sleep.vbs
start /wait sleep.vbs
CommandApp_USBRelay 6QMBS close 01
del /f /s /q sleep.vbs

