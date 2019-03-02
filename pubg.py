# coding=utf-8
import threading
from pynput.mouse import Button, Listener, Controller
from pynput import keyboard
import time
 
# 记录操作指令
# 射击
shoot = 0
# 倍镜
scope = -1
# 开启压枪状态
status = 1
 
# 鼠标控制器
controller = Controller()
 
"""
鼠标事件
"""
def mouse_click(x, y, button, pressed):
    global shoot
    global scope
    if pressed:
        # 开启倍镜
        if button == Button.right:
            scope = - scope
        # 开始射击
        if button == Button.left:
            shoot = 1
    # 结束射击
    if not pressed and button == Button.left:
        shoot = 0
 
# 监控鼠标位置
def mouse_move(x, y):
    print (x,y)
 
"""
键盘事件
"""
def keyboard_release(key):
    global status
    if key == keyboard.Key.backspace:
        # 更改压枪状态
        status = -status
"""
监听事件方法
"""
def mouseListener():
    with Listener(on_click=mouse_click, on_move=mouse_move) as listener:
        listener.join()
 
def keyboardListener():
    with keyboard.Listener(
            on_release=keyboard_release) as listener:
        listener.join()
 
def main():
    threading._start_new_thread(mouseListener, ()) 
    threading._start_new_thread(keyboardListener, ())
    # 循环监听各状态并控制鼠标
    while 1:
        if shoot == 1 and scope == -1 and status == 1:
            time.sleep(0.2) # 根据一般的子弹射速有节奏的压枪
            controller.move(0, +15)
        elif shoot == 1 and scope == 1 and status == 1:  # 开启倍镜，增加压枪幅度
            time.sleep(0.2)
            controller.move(0, +25)
 
 
if __name__ == '__main__':
    main()
