from screen_search import *
import pyautogui
import time
import os
import pandas as pd
import random
import pytesseract
import torch
from Browsernew import newbrowseruser as nbu
from Capatcha import CPATCHA

# CMD MAX WINDOW AND MOVE TO LEFT BEFORE STARTING MAIN SCRIPT
print("Maxing Window")
fw1 = pyautogui.getActiveWindow()
fw1.maximize()
time.sleep(3)
# Slap Window to Right of screen
print('Moving Window to the right')
pyautogui.hotkey('win', 'left')
time.sleep(2)

# TEXT LOGIC
tesspath = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if not os.path.exists(tesspath):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
else:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# YOLO LOGIC
model = torch.hub.load("ultralytics/yolov5", "custom", path="yolov5/run8-v1.pt",force_reload=True)
model.conf = 0.82


# THINGS TO EDIT IF MOVED!!!!
# USER DATABASE
database = 'data/database2.csv'
time.sleep(1)
# MAX WINDOW AND MOVE TO RIGHT
def maxmoveright():
    # PRESS ENTER FOR RESTORE
    time.sleep(3)
    restore = pyautogui.locateCenterOnScreen("img/restore2.png")
    time.sleep(3)
    if restore:
        time.sleep(3)
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.press('enter')
    restore2 = pyautogui.locateCenterOnScreen("img/restore.png")
    time.sleep(3)
    if restore2:
        time.sleep(3)
        pyautogui.click(restore2)
    print("Maxing Window")
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(3)
    # Slap Window to Right of screen
    print('Moving Window to the right')
    pyautogui.hotkey('win', 'right')
    time.sleep(2)
# LOGIN LOGIC
def Login():
    print("FOUND LOGIN")
    print("LOGGING IN ")
    loginns = pyautogui.locateCenterOnScreen("img/register.PNG")
    pyautogui.click(loginns)
    time.sleep(5)

    # Type USERNAME
    print("typing username")
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    print("typing password")
    pyautogui.typewrite("@Starwars2")

    # MAX LOGIN WINDOW TO READ CAPTCHA
    # press max window
    pyautogui.click(539, 11)

# MAIN SEARCH LOOP
bravepath1 = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
if not os.path.exists(bravepath1):
    a = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
else:
    a = 'cmd /c  start "" /max /b "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --profile-directory="Profile '


# Anchor start
b = '" https://presearch.com/search?q=dolphins'
start1 = a + str(1) + b
os.system(start1)
maxmoveright()
nbu()
print("Min anchor window")
pyautogui.click(901, 12)
# DAYS COUNTER
count = 1
# COUNT FOR BRAVE USERS
minercount = 0
# print (df)
while count < 35:

    # PRESEARCH ACCOUNTS COUNT
    count3 = 1
    while count3 < 120:

        # GET DATABASE INFO FOR PRESEARCH LOGIN DATA
        data = pd.read_csv(database)  # read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of
        # the path + ".csv"
        df = pd.DataFrame(data, columns=['username'], )
        username = df.iloc[count3, 0]
        time.sleep(2)

        # IF FILE FOR DIFFERENT BRAVE .EXE LOCATIONS ACROSS SERVERS
        bravepath = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        if not os.path.exists(bravepath):
            a = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        else:
            a = 'cmd /c  start "" /max /b "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --profile-directory="Profile '

        print(" RUNNING DAY " + str(count))
        print("RUNNING PRESEARCH ACCOUNT " + str(count3))

        b = '" https://presearch.com/search?q=greyiaceae%2C'
        # START MINERS THEN MAX IT
        start = a + str(count3) + b
        if count == 1:
            os.system(start)
            time.sleep(3)
            maxmoveright()
        # RUN THE LOGIC FOR CREATING NEW BRAVE USER AND MAKE SURE 10 is set, adds are on , and autocontrib is off
            nbu()
            #
            os.system(start)
            time.sleep(3)
            


        if count > 1:
            # SUM COUNTING
            sum = count3 + minercount
            print("STARTING BRAVE USER NUMBER " + str(sum))
            start2 = a + str(count3 + minercount) + b
            time.sleep(3)
            os.system(start2)
            maxmoveright()
            # NEW USER BROSWER
            nbu()
            os.system(start2)
            time.sleep(3)
            

        time.sleep(6)



        # SEARCH SCREEN FOR LOGIN
        print("REFRESHING WINDOW TO MAKE SURE LOGGED IN OR NOT ")
        pyautogui.press('f5')
        time.sleep(3)
        print("Searching For Login Avatar")
        search = Search("img/loggedin.PNG")
        pos = search.imagesearch()
        # IF LOGGED IN ALREADY DO :
        if pos[0] != -1:
            print("FOUND ALREADY LOGGED IN ")

        # LOGIN NOT FOUND DO
        else:
            print("LOGOUT NOT FOUND.")
            # LOGIN IF LOGGED OUT
            print("LOGIN NOT FOUND,.. ALREADY LOGGED OUT ")
            # SEARCH SCREEN FOR LOGIN
            print("Searching For REGISTER OR LOGIN")
            search3 = Search("img/register.PNG")
            pos3 = search3.imagesearch()
            # LOGIN
            if pos3[0] != -1:
                Login()
                print("Clicking I AM Human")
                pyautogui.click(332, 450)
                time.sleep(2)
                CPATCHA()

        # SEARCH LOOP
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

        #END START OVER
        print("sleep between accounts")
        time.sleep(10)

        # CLOSE WINDOWS AND EXIT TABS
        print("closing all windows and exiting tabs for restart")
        browserExe = "brave.exe"
        os.system("taskkill /f /im " + browserExe)
        # EXIT TO KEEP RUNNING IN BACKGROUND TEST !
        #pyautogui.hotkey('alt', 'f4')
        time.sleep(2)
        # Close all logic
        closeall = pyautogui.locateOnScreen("img/closeall.png")
        time.sleep
        if closeall:
            print("Clicking Dont ask me again")
            pyautogui.click(633, 188)
            print("clicking Close All")
            time.sleep(2)
            pyautogui.click(closeall)
        print("RAN NUMBER", count3)

        # ADD TO PRE SEARCH COUNT LOOP
        count3 += 1

    print("sleep between accounts")
    time.sleep(10)
    # CLOSE WINDOWS AND EXIT TABS
    print("closing all windows and exiting tabs for restart")
    # browserExe = "brave.exe"
    # os.system("taskkill /f /im " + browserExe)
    # EXIT TO KEEP RUNNING IN BACKGROUND TEST !
    pyautogui.hotkey('alt', 'f4')
    closeall = pyautogui.locateOnScreen("img/closeall.png")
    time.sleep
    if closeall:
        pyautogui.click(633, 188)
        time.sleep(2)
        pyautogui.click(closeall)
    print("RAN DAY NUMBER " + str(count))
    # ADDING PRESEARCH LOOP TO BRAVE USERS COUNT 
    minercount += 120
    count += 1
