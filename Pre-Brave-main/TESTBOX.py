## LEFTOVER CODE FOR PRESEARCH MINING MAY USE LATER
from screen_search import *
import pyautogui
import time
import os
import keyboard
import pandas as pd
print("CLICKING captcha")
time.sleep(8)
from Capatcha import CPATCHA
robot = pyautogui.locateOnScreen('test.png')
print(robot)
CPATCHA()