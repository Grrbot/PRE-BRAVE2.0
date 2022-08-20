## LEFTOVER CODE FOR PRESEARCH MINING MAY USE LATER
from screen_search import *
import pyautogui
import time
import os
import keyboard
import pandas as pd
print("CLICKING captcha")
time.sleep(5)
print(pyautogui.locateOnScreen("test.png"))
# from Capatcha import CPATCHA
time.sleep(1)
text = " choose canine"
canine = "canine"
if canine in text:            
            print("POINTING AI TO FIND ALL CAININE IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI            
            dir_path = 'runs/detect/exp/crops/dog/'            
            if os.path.exists(dir_path):           
                # Iterate directory
                res = os.listdir(dir_path)
                print(res)
                for x in range(len(res)):
                    print(res[x])
                    # CLICK THE IMAGES FOUND IN FILE
                    var2 = dir_path + res[x]
                    var1 = pyautogui.locateOnScreen(var2)
                    pyautogui.moveTo(var1)
                    print("LOOKING FOR CROPPED IMAGE")
                    print(var1)
                    print("CLICKING IMAGE")
                    pyautogui.click()
                    time.sleep(1)
            dir_path2 = 'runs/detect/exp/crops/dog with collar/'           
            if os.path.exists(dir_path2):    
                print("DOG WITH COLLAR")       
                # Iterate directory
                res2 = os.listdir(dir_path2)
                print(res2)
                for x in range(len(res2)):
                    print(res2[x])
                    # CLICK THE IMAGES FOUND IN FILE
                    var2 = dir_path2 + res2[x]
                    var1 = pyautogui.locateOnScreen(var2)
                    pyautogui.moveTo(var1)
                    print("LOOKING FOR CROPPED IMAGE")
                    print(var1)
                    print("CLICKING IMAGE")
                    pyautogui.click()
                    time.sleep(1)
# CPATCHA()