# coding:utf-8

import pyHook
import pythoncom
from time import *

def onMouseEvent(event):
   print ("MessageName:",event.MessageName)
   print ("Message:", event.Message)
   print ("Time:", event.Time)
   print ("Window:", event.Window)
   print ("WindowName:", event.WindowName)
   print ("Position:", event.Position)
   print ("Wheel:", event.Wheel)
   print ("Injected:", event.Injected)
   print("---")

   return True

def onKeyboardEvent(event):
    # 监听键盘事件
    print ("MessageName:", event.MessageName)
    print ("Message:", event.Message)
    print ("Time:", event.Time)
    print ("Window:", event.Window)
    print ("WindowName:", event.WindowName)
    print ("Ascii:", event.Ascii, chr(event.Ascii))
    print ("Key:", event.Key)
    print ("KeyID:", event.KeyID)
    print ("ScanCode:", event.ScanCode)
    print ("Extended:", event.Extended)
    print ("Injected:", event.Injected)
    print ("Alt", event.Alt)
    print ("Transition", event.Transition)
    print ("---")
    # 同鼠标事件监听函数的返回值
    return True
def onMouse_leftdown(event):
    # 监听鼠标左键按下事件
    print ("left DOWN DOWN")
    return True
    # 返回 True 表示响应此事件，False表示拦截

def onMouse_leftup(event):
    # 监听鼠标左键弹起事件
    print ("left UP UP UP")
    return True

def main():
    # 创建一个：钩子“管理对象
    hm = pyHook.HookManager()
    # 监听所有的键盘事件
    hm.KeyDown = onKeyboardEvent
    #设置键盘”钩子“
    hm.HookKeyboard()
    # 监听鼠标事件
    # hm.MouseAll = onMouseEvent
    hm.MouseLeftDown = onMouse_leftdown
    hm.MouseLeftUp = onMouse_leftup
    # 设置鼠标钩子
    hm.HookMouse()
    # 进入循环侦听，需要手动进行关闭，否则程序将一直处于监听的状态。可以直接设置而空而使用默认值
    pythoncom.PumpMessages()
    # 我也不知道为什么直接放置到main函数中不管用

if __name__ == "__main__":
    main()
