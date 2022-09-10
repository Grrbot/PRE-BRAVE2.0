from tkinter.tix import Tree
from unittest import skipIf
from screen_search import *
import pyautogui
import time
import os
import pytesseract
import cv2
import numpy as np
import torch
import shutil
import random
from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
# TEXT LOGIC
tesspath = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if not os.path.exists(tesspath):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
else:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# YOLO LOGIC
model = torch.hub.load("ultralytics/yolov5", "custom", path="yolov5/run8-v1.pt", force_reload=True)
model.conf = 0.82


# THINGS TO EDIT IF MOVED!!!!
# USER DATABASE
database = 'data/database2.csv'
# GIF LOGIC 
def GIF():
    oldtime = time.time()
    gif_list = ['gifs/giphy.gif','gifs/suckit.gif','gifs/3.gif','gifs/4.gif','gifs/5.gif']
    gif = random.choice(gif_list)
    bear = r'img/' + str(gif)
    layout = [[sg.Image(key='-IMAGE-')]]
    window = sg.Window('SUCK IT PRE', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True, keep_on_top=True)
    sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(bear))]
    interframe_duration = Image.open(bear).info['duration']
    
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    
    while True:
        
        for frame in sequence:
            event, values = window.read(timeout=interframe_duration)  
            window.move(x, y)        
            if time.time() - oldtime > 6:
                print ("EYYY")
                break           
            time.sleep(.09)
            window['-IMAGE-'].update(data=frame)
        window.close()
        break
# CHECKIF LOGIN LOGIN WORKED
def CHECKifworked():
    # CHECK IF FAILED AND RETRY ENTIRE SCRIP
    while True:
        iamhuman = pyautogui.locateOnScreen("img/imhuman.png")
        if iamhuman:
            time.sleep(2)
            print(" Checking if I AM HUMAN IS ON SCREEN")
            pyautogui.click(332, 450)
            CPATCHA()
        
        # LOOK FOR VERIFY BUTTON AND CLICK
        time.sleep(1)
        verify = pyautogui.locateOnScreen("img/verify.png")
        time.sleep(2)
        if verify:
            print("PRESSING VERIFY AND FINISHING UP")
            pyautogui.click(verify)
            time.sleep(10)            
            skip = pyautogui.locateOnScreen("img/skip.png")
            if skip:
                print("DIDNT WORK TRYING AGAIN")
                CPATCHA()
                break
            # CLICK LOGIN
            print("CLICKING LOGIN")
            pyautogui.click(535, 514)
            time.sleep(3)
            # RUNNING GIF
            GIF()
        login2 = pyautogui.locateOnScreen("img/login.png")
        time.sleep(4)
        if login2:
            print("PRESSING LOGIN IF NOT CLICKED BEFORE")
            time.sleep(1)
            pyautogui.moveTo(login2)
            pyautogui.click()
            time.sleep(2)
            break
        else:
            break            
# MAIN CAPTHCA LOGIC
def CPATCHA():
    # WHILE TRUE LOOP FOR FINDING THE EXACT SEARCH TERMS OUR DATASET FAVORS
    while True:
        print("RUNNING WHILE TRUE LOOP 1 ")
        # DELETE FOLDER SO I CAN PULL IMAGES

        print(" OPENING FOLDER TO DELETE")
        # checking whether folder exists or not
        files = 'runs/detect/'
        try:
            shutil.rmtree(files)
        except OSError as e:
            print("Error: %s : %s" % (files, e.strerror))

        # IMG TO TEXT TO GET TARGET TEXT

        # Take Screen Shot of TARGET
        print('TAKING SCREENSHOT OF TARGET TEXT')
        img = pyautogui.screenshot(region= (372, 136, 263, 79)) #(374, 146, 230, 57))
        time.sleep(1)

        # CONVERT IMAGE TO CV2 READABLE
        print('CONVERTING IMAGE')
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


        # SAVE IMAGE TO FILE NAMED TARGET.PNG
        print('Saving image to target.png')
        cv2.imwrite("target.png", image)

        # READ IMAGE WITH CV2
        print('READING IMAGE')
        img = cv2.imread("target.png")
        time.sleep(1)
        # GET TEXT FROM TARGET.PNG TO SEE WHAT TO DRAG TO
        print('EXTRACTING TEXT FROM IMAGE')
        text = pytesseract.image_to_string(img, lang='eng')
        time.sleep(2)

        # CHECK IF TEXT WAS FOUND
        print('FOUND : \"', text, '\"')
        train = "train"
        truck = "truck"
        airplane = "airplane"
        bike = "bike"
        motorcycle = "motorcycle"
        bus = "motorbus"
        seaplane = "seaplane"
        boat = "boat"
        car = "car"
        livingroom = "living room"
        conference = "conference"
        bedroom = "bedroom"
        lion = "lion"
        lionmane = "lion with mane"
        lionwith = "lion with"
        femalelion = "female lion"
        dog = "dog"
        dogcollar = "dog with a collar"
        smilingdog = "smiling dog"
        dogwith = "dog with"
        cat = "cat"
        giraffe = "giraffe"
        elephants = "elephant"
        bird = "bird"
        birdflying = "bird flying"
        parrot = "parrot"
        horsefacing = "horse facing"
        horsewith = "horse with"
        horse = "horse"
        canine = "canine"

        # Wait for images to show
        print("waiting for images to show")
        time.sleep(3)
        print("Taking ScreenShot For Cropping")

        # SCREEN SHOT OF IMAGES
        capimg = pyautogui.screenshot("img.png") #region=(363, 245, 392, 398))
        time.sleep(2)
        results = model(capimg)
        crops = results.crop(save=True)
        
        # RUN CLICK Command BASED ON TARGET VARIABLE
        if train in text:
            print("LOOKING FOR TRAINS TO CROP")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/train/'
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
                time.sleep(1)
                pyautogui.click()            
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()

            break
        if truck in text:
            print("LOOKING FOR TRUCKS")
            print("POINTING AI TO FIND ALL TRUCK IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/truck/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if airplane in text:
            print("LOOKING FOR AIRPLAINS")
            print("POINTING AI TO FIND ALL AIRPLANE IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/plane/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if bike in text:
            print("LOOKING FOR BIKES")
            print("POINTING AI TO FIND ALL BIKE IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/bike/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if motorcycle in text:
            print("LOOKING FOR MOTORCYCLES")
            print("POINTING AI TO FIND ALL MOTORCYCLES IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/motorcyle/'
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
                time.sleep(2)
                print("CLICKING IMAGE")
                pyautogui.click()
                time.sleep(1)
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if bus in text:
            print("LOOKING FOR BUSSES")
            print("POINTING AI TO FIND ALL BUS IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/bus/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if seaplane in text:
            print("LOOKING FOR SEAPLANES")
            print("POINTING AI TO FIND ALL SEAPLANES IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/seaplane/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if boat in text:
            print("LOOKING FOR boats")
            print("POINTING AI TO FIND ALL SEAPLANES IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/boat/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if car in text:
            print("POINTING AI TO FIND ALL CAR IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/car/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if livingroom in text:
           
            print("POINTING AI TO FIND ALL LIVING ROOM IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/livingroom/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if conference in text:
            
            print("POINTING AI TO FIND ALL CONFERENCE ROOM IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/conference room/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if bedroom in text:
            
            print("POINTING AI TO FIND ALL BEDROOM IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/bedroom/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        # IF NEW SENTINCE INTRODUSED       
        if lion in text:   
            while True:
                if lionwith in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA()
                    break
                if femalelion in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA() 
                    break                       
                print("POINTING AI TO FIND ALL LION IMAGES")
                # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI            
                dir_path = 'runs/detect/exp/crops/lion/'            
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
                dir_path2 = 'runs/detect/exp/crops/lion with mane on neck/'            
                if os.path.exists(dir_path2):           
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
                IFNEXT = pyautogui.locateOnScreen("img/next.png")
                if IFNEXT:
                    pyautogui.click(IFNEXT)
                    CPATCHA()
                    CHECKifworked()
                    break
                else:
                    CHECKifworked()
                break
            break
         # IF NEW SENTINCE INTRODUSED         
        if dog in text:
            while True:
                # DOG VARIABLES 
                if smilingdog in text:            
                    print("POINTING AI TO FIND ALL SMILING DOGOS IMAGES")
                    # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
                    dir_path = 'runs/detect/exp/crops/smiling dog/'
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
                    IFNEXT = pyautogui.locateOnScreen("img/next.png")
                    if IFNEXT:
                        pyautogui.click(IFNEXT)
                        CPATCHA()
                        CHECKifworked()
                        break
                    else:
                        CHECKifworked()
                    break
                if dogcollar in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA()
                    break
                if dogwith in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA()
                    break
                # RUNNING JUST DOG 
                print("POINTING AI TO FIND ALL DOG IMAGES")
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
                IFNEXT = pyautogui.locateOnScreen("img/next.png")
                if IFNEXT:
                    pyautogui.click(IFNEXT)
                    CPATCHA()
                    CHECKifworked()
                    break
                else:
                    CHECKifworked()
                break
            break
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if giraffe in text:
           
            print("POINTING AI TO FIND ALL GIRAFFE IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/giraffe/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if elephants in text:
            
            print("POINTING AI TO FIND ALL ELEPHANTS IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/elephants/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        if bird in text:
            while True:
                if birdflying in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA()
                    break
                print("POINTING AI TO FIND ALL BIRD IMAGES")
                # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
                dir_path = 'runs/detect/exp/crops/parrot/'
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
                IFNEXT = pyautogui.locateOnScreen("img/next.png")
                if IFNEXT:
                    pyautogui.click(IFNEXT)
                    CPATCHA()
                    CHECKifworked()
                    break
                else:
                    CHECKifworked()
                break
            break
        if parrot in text:
            
            print("POINTING AI TO FIND ALL PARROT IMAGES")
            # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
            dir_path = 'runs/detect/exp/crops/parrot/'
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
            IFNEXT = pyautogui.locateOnScreen("img/next.png")
            if IFNEXT:
                pyautogui.click(IFNEXT)
                CPATCHA()
                CHECKifworked()
            else:
                CHECKifworked()
            break
        # CONTAINS VAIRABLES  
        if horse in text:
            while True:
                if horsefacing in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA()
                    break
                if horsewith in text:
                    skip = pyautogui.locateOnScreen("img/skip.png")
                    time.sleep(2)
                    print("NEW VARIABLE CLICKING SKIP TO GET ONE IN DATABASE")
                    pyautogui.click(skip)
                    time.sleep(3)
                    CPATCHA()
                    break
                print("LOOKING FOR HORSES")
                print("POINTING AI TO FIND ALL HORSE IMAGES")
                # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
                dir_path = 'runs/detect/exp/crops/horse/'
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
                IFNEXT = pyautogui.locateOnScreen("img/next.png")
                if IFNEXT:
                    pyautogui.click(IFNEXT)
                    CPATCHA()
                    CHECKifworked()
                    break
                else:
                    CHECKifworked()
                break
            break
                
            
        else:
            # PRESSING SKIP TO FIND RIGHT TEXT
            print("No Targets in Database Found")
            skip = pyautogui.locateOnScreen("img/skip.png")
            time.sleep(2)
            if skip:
                while True:
                    print("taking screenshot of target area for data collection")
                    if skip:
                        time.sleep(1)
                        iamhuman = pyautogui.locateOnScreen("img/imhuman.png")
                        if iamhuman:
                            pyautogui.click(iamhuman)
                            time.sleep(3)

                        # Click Skip to go to the next option
                        print("CLICKING SKIP TO GET WHAT I WANT")
                        pyautogui.click(skip)
                        time.sleep(2)
                        # Take Screen Shot of TARGET
                        print('TAKING SCREENSHOT OF TARGET TEXT')
                        img = pyautogui.screenshot(region=(375, 146, 224, 57))
                        time.sleep(2)
                        # CONVERT IMAGE TO CV2 READABLE
                        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                        time.sleep(1)
                        # SAVE IMAGE TO FILE NAMED TARGET.png
                        cv2.imwrite("target.png", image)
                        time.sleep(1)
                        # READ IMAGE WITH CV2
                        img = cv2.imread("target.png")
                        time.sleep(1)
                        # GET TEXT FROM TARGET.PNG TO SEE WHAT TO DRAG TO
                        print('EXTRACTING TEXT FROM IMAGE')
                        text2 = pytesseract.image_to_string(img, lang='eng')
                        # CHECK IF TEXT WAS FOUND
                        print('FOUND : \"', text2, '\"')
                        
                        # RUN CLICK CMD BASED ON TARGET VARIABLE
                        textlist3 = ["bus","train","boat","plane","car","seaplane","bike","motorbike","living room","lion","lion with mane","bridge","dog","dog with collar","smiling dog","giraffe","elephants","bedroom","conference","bird","parrot","horse","truck"]                     
                        target3 = [ele for ele in textlist3 if(ele in text2)]
                        print("Does string contain any list element : " + str(bool(target3)))
                        lists = str(bool(target3))
                        # print(res)
                        if lists == "True":
                            print(" FOUND TARGET ")
                            print(" FOUND TARGETS", target3)
                            break

                    else:
                        break
            else:
                break
