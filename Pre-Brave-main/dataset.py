import pyautogui
import time
import os
time.sleep(3)
count = 500
while count < 750:
    time.sleep(1)
    pyautogui.click(332, 442)
    time.sleep(6)
    pyautogui.screenshot('dataset/img' + str(count) + '.png')
    pyautogui.click(271, 416)
    time.sleep(2)
    count += 1
