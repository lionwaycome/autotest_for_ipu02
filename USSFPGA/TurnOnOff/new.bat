D:
cd D:\Program Files\YY\Tools\USBRelay\

echo wscript.sleep 100>sleep.vbs

CommandApp_USBRelay 6QMBS close 5
echo %date%%time%


start /wait sleep.vbs
CommandApp_USBRelay 6QMBS open 5
echo %date%%time%

del /f /s /q sleep.vbs

pause
