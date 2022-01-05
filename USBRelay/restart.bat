@echo off
cd "D:\TestStand_IPU02\dist\USBRelay"

echo wscript.sleep 5000>sleep.vbs

CommandApp_USBRelay 6QMBS open 1



start /wait sleep.vbs
CommandApp_USBRelay 6QMBS close 1


del /f /s /q sleep.vbs

exit 