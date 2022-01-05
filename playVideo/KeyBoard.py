# _*_ coding:UTF-8 _*_
import win32api
import win32con
import win32gui
from ctypes import *
import time
key_map  = {
  'shift':0x10,
  'right_arrow':0x27,
  'home':20,
  'win':91
  }
def key_down(key):
    """
    函数功能：按下按键
    参    数：key:按键值
    """
    vk_code = key_map[key]
    win32api.keybd_event(vk_code,win32api.MapVirtualKey(vk_code,0),0,0)
def key_up(key):
    """
    函数功能：抬起按键
    参    数：key:按键值
    """
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)
def key_press(key):
    """
    函数功能：点击按键（按下并抬起）
    参    数：key:按键值
    """
    key_down(key)
    time.sleep(0.02)
    key_up(key)
def MoveVideo():
        key_down("shift")
        key_down("win")
        key_press("right_arrow")
        time.sleep(0.02)
        key_up("shift")
        key_up("win")
if __name__ == "__main__":
    MoveVideo()
