import pyautogui
import time

pyautogui.FAILSAFE = True

time.sleep(3)
while True:
    pyautogui.moveTo(940, 540, duration=0.25)
    time.sleep(0.5)
    pyautogui.click(940, 540)
    time.sleep(12)
    pyautogui.moveTo(1150, 600, duration=0.25)
    pyautogui.click(1150, 600)
    time.sleep(53)
    pyautogui.moveTo(640, 590, duration=0.25)
    pyautogui.click(640, 590)
    time.sleep(1)
    pyautogui.click(640, 590)
    time.sleep(1)
    pyautogui.click(640, 590)
    time.sleep(1)
    pyautogui.click(640, 590)
