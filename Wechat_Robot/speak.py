
# coding:utf-8
import sys
import importlib
importlib.reload(sys)
#sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/6'
#    __Desc__ = 文字转语音输出
import pyttsx
engine = pyttsx.init()
engine.say('hello world')
engine.say('中文')
engine.runAndWait()
# 朗读一次
engine.endLoop()

