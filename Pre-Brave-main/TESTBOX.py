## LEFTOVER CODE FOR PRESEARCH MINING MAY USE LATER
from screen_search import *
import pyautogui
import time
import os
import keyboard
import pandas as pd
count2 = 1
while count2 < 32:
            # REFRESH PAGE FOR 403 FORBIDIN
            pyautogui.press('f5')
            time.sleep(3)
            # FIND SEARCH WORD
            with open('data/words.csv') as f:
                words = f.read().split()
                my_pick = random.choice(words)
                my_pick2 = my_pick.replace(",", "", 1)
            # MOVE TO SEARCH AREA TO RUN SEARCH LOOP
            # click small x to clear search
            print(" Deleting Search terms ")
            pyautogui.moveTo(927, 108)
            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            # GETTING SEARCH TERMS
            print("Getting Search Terms")
            print("Typing Search Term")
            pyautogui.typewrite(my_pick2)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(3)
            print("Ran Search " + str(count2))
            count2 += 1