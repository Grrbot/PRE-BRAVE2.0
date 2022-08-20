import csv
import os
from datetime import datetime
from screen_search import *
import time
import cv2
import numpy as np
import pyautogui
import pytesseract
pyautogui.FAILSAFE = False
currentMonth = datetime.now().month
def vpn_change():
    # Run Vpn Change IP
    os.startfile(r"C:\Program Files\IPVanish VPN\IPVanish.exe")
    time.sleep(2)
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(3)
    pyautogui.hotkey('win', 'left')
    time.sleep(7)
    pyautogui.click(699, 67, duration=0.25)
    time.sleep(6)
    pyautogui.click(549, 699, duration=0.25)
    time.sleep(7)
    pyautogui.press('down', presses=1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(693, 63, duration=0.256)
    time.sleep(3)
    pyautogui.click(718, 13, duration=0.25)
    time.sleep(40)
# ADD Pytesseract to file
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# pyautogui.FAILSAFE
pyautogui.hotkey("win", "m")
count = 1
while count < 1000:
    time.sleep(1)
    print('RUNNING NUMBER ' + str(count))
    # *******BLOCK OF DRAG COMMANDS*****
# DRAG to brave trianlge FUNCTION

    def tri_drag():

        bigtt = Search("bigtt.png")
        bigtt2 = bigtt.imagesearch()
        print("position : ", bigtt2)
        pyautogui.moveTo(bigtt2)
        tri = Search('tt.png')
        tt = tri.imagesearch()
        print("TRIANGLE TARGET FOUND : ", tt)
        pyautogui.dragTo(tt, duration=0.5)

    # DRAG TO SQUARE

    def sqr_drag():
        bigtt = Search("bigtt.png")
        bigtt2 = bigtt.imagesearch()
        print("position : ", bigtt2)
        pyautogui.moveTo(bigtt2)
        squaretrg = Search('square.png')
        sqr = squaretrg.imagesearch()
        print("SQUARE TARGET FOUND : ", sqr)
        pyautogui.dragTo(sqr, duration=0.5)


    # DRAG TO CIRCLE


    def crcl_drag():
        bigtt = Search("bigtt.png")
        bigtt2 = bigtt.imagesearch()
        print("position : ", bigtt2)
        pyautogui.moveTo(bigtt2)
        ci = Search('circle.png')
        crcl = ci.imagesearch()
        print("TRIANGLE TARGET FOUND : ", crcl)
        pyautogui.dragTo(crcl, duration=0.5)

# END OF BLOCK OF DRAG COMMANDS

    # concataniate for brave start
    start = r'cmd /c start "" /b "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe" --profile-directory="Profile "'
    b = count
    os.system(start + str(b))
    print("Running Start", start)

    # Run BRAVE BROWSER WITH USERS
    # os.system(start)
    time.sleep(10)

    # FIND IF STUPID RESOTE PAGES BOX IS OPEN HATE THIS PAGE LOL !!!!!
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
    else:
        print("image not found")

    # MAXAMIZE
    time.sleep(2)
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(3)
    # make sure current window selected
    # Slap Window to Right of screen
    # print('Moving Window to the right')
    # pyautogui.hotkey('win', 'right')
    pyautogui.hotkey('win', 'left')
    time.sleep(3)

    # Click Hamnburger Menu
    print('clicking menu')
    pyautogui.click(x=486, y=55, duration=0.25)
    time.sleep(3)

    # Click Brave Rewards Option
    print('Clicking Brave Rewards')
    pyautogui.click(x=267, y=187, duration=0.25)
    time.sleep(5)

    # Move browser to see
    pyautogui.click(466, 717, duration=0.25)
    pyautogui.click(466, 717, duration=0.25)
    time.sleep(15)
    pyautogui.click(504, 94, duration=0.26)

    # Click to clear "oops "
    pyautogui.click(213, 624)
    time.sleep(4)
    # Click Claim
    clmcount = 1
    while clmcount < 5:
        # Move browser to see
        pyautogui.click(466, 717, duration=0.25)
        pyautogui.click(466, 717, duration=0.25)
        time.sleep(15)
        pyautogui.click(504, 94, duration=0.26)
        time.sleep(3)
        pyautogui.click(470, 202)
        claim = Search('claim.png')
        clm = claim.imagesearch()
        clm2 = claim.imagesearch()
        if clm[0] != -1:
            print("position : ", clm)
            click = pyautogui.moveTo(clm)
            pyautogui.click(click, duration=0.4)
            time.sleep(3)
    # elif clm2[0] != -1:
        # print("position : ", clm2)
        # click2 = pyautogui.moveTo(clm2)
        # pyautogui.click(click2, duration=0.4)

        else:
            print("CLAIM not found")
            time.sleep(3)
        time.sleep(10)
        pyautogui.click(503, 699, duration=0.26)
        pyautogui.click(503, 699, duration=0.26)
        pyautogui.click(503, 699, duration=0.26)
    # Take SCreen Shot of TARGET
        print('TAKING SCREENSHOT')
        image = pyautogui.screenshot(region=(287, 306, 144, 62))
        time.sleep(3)

    # CONVERT IMAGE TO CV2 READABLE
        print('CONVERTING IMAGE')
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # SAVE IMAGE TO FILE NAMED TARGET.PNG
        print('saving image to target.png')
        cv2.imwrite("target.png", image)
        # READ IMAGE WITH CV2
        print('READING IMAGE')
        img = cv2.imread("target.png")

        # GET TEXT FROM TARGET.PNG TO SEE WHAT TO DRAG TO
        print('EXTRACTING TEXT FROM IMAGE')
        text = pytesseract.image_to_string(img, lang='eng')

        # CHECK IF TEXT WAS FOUND
        print('FOUND', text)
        circle = "circle"
        square = "square"
        triangle = "triangle"

    # RUN DRAG COMMANDS BASED ON TARGET VARIABLE
        if circle in text:
            print("RUNNNING CICRLE DRAG")
            crcl_drag()
        if square in text:
            sqr_drag()
        if triangle in text:
            tri_drag()

        time.sleep(10)
        # Click OK
        pyautogui.click(238, 464)

        clmcount += 1

    # FIND TOTAL BAT GENERATED FOR MONTH


    # PRINT BAT TOTAL PER MINER


    # CLICK OK
    ok = pyautogui.locateCenterOnScreen('ok.png')
    pyautogui.click(ok, duration=0.25)
    time.sleep(3)

    # CLICK EXIT BROWSER
    pyautogui.click(485, 12, duration=0.25)

    # vpn change
    if count == 45:
        vpn_change()
    if count == 86:
        vpn_change()
    if count == 129:
        vpn_change()
    if count == 172:
        vpn_change()
    if count == 215:
        vpn_change()
    if count == 258:
        vpn_change()
    if count == 301:
        vpn_change()
    if count == 344:
        vpn_change()
    if count == 387:
        vpn_change()
    if count == 430:
        vpn_change()
    if count == 473:
        vpn_change()
    if count == 516:
        vpn_change()
    if count == 559:
        vpn_change()
    if count == 602:
        vpn_change()
    if count == 645:
        vpn_change()
    if count == 688:
        vpn_change()
    if count == 731:
        vpn_change()
    if count == 774:
        vpn_change()
    if count == 817:
        vpn_change()
    if count == 860:
        vpn_change()
    if count == 903:
        vpn_change()
    if count == 946:
        vpn_change()
    if count == 989:
        vpn_change()

    print("FINSIHED COLLECTING REWARD FOR WALLET", count)
    count += 1  # This is the same as count = count + 1
    # Gap

# TIPPING!!!!!!

from screen_search import *
import pyautogui
import time
import os
def vpn_change():
    # Run Vpn Change IP
    os.startfile(r"C:\Program Files\IPVanish VPN\IPVanish.exe")
    time.sleep(2)
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(3)
    pyautogui.hotkey('win', 'left')
    time.sleep(7)
    pyautogui.click(699, 67, duration=0.25)
    time.sleep(6)
    pyautogui.click(549, 699, duration=0.25)
    time.sleep(7)
    pyautogui.press('down', presses=1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(693, 63, duration=0.256)
    time.sleep(3)
    pyautogui.click(718, 13, duration=0.25)
    time.sleep(40)


count1 = 1
while count1 < 1000:
    time.sleep(2)

    print('RUNNING NUMBER ' + str(count1))
    # *******BLMOCK OF DRAG COMMANDS*****

    # END OF BLOCK OF DRAG COMMANDS

    # concataniate for brave start
    a = 'cmd /c  start "" /max /b "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --profile-directory="Profile '
    b = '" www.candyshop.space'
    start = a + str(count1) + b
    print("Running Start", start)

    # Run BRAVE BROWSER WITH USERS
    os.system(start)
    time.sleep(20)

    # FIND IF STUPID RESOTE PAGES BOX IS OPEN HATE THIS PAGE LOL !!!!!
    search = Search("restore.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        clk = pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click(clk, duration=0.4)
    else:
        print("RESTORE not found")

    # MAXAMIZE
    print("maxing window")
    time.sleep(2)
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(7)
    pyautogui.hotkey("win", "left")
    # Click Teamviers Dump Thing
    # pyautogui.click(x=661, y=422)
    # click rewards triangle
    pyautogui.click(415, 52, duration=0.25)
    time.sleep(11)
    # Click Exit Backup Wallet Popup
    # pyautogui.click(406, 94, duration=0.24)
    # pyautogui.click(406, 94, duration=0.24)
    # pyautogui.click(406, 94, duration=0.24)
    # click donate Now
    pyautogui.click(223, 392, duration=0.2)
    time.sleep(2)
    pyautogui.click(x=116, y=446)
    time.sleep(1)
    pyautogui.click(x=116, y=446)
    time.sleep(5)
    # click send tip 10
    pyautogui.press('tab', presses=10)
    time.sleep(3)
    # Click Send
    pyautogui.press('enter')
    # click exit
    pyautogui.press('esc')

    # start tip 1 loop
    tiploop = 0
    while tiploop <= 11:
        pyautogui.click(415, 52, duration=0.25)
        time.sleep(11)
        # Click Exit Backup Wallet Popup
        pyautogui.click(406, 94, duration=0.24)
        pyautogui.click(406, 94, duration=0.24)
        pyautogui.click(406, 94, duration=0.24)
        # click donate Now
        pyautogui.click(223, 392, duration=0.2)
        time.sleep(2)
        pyautogui.click(x=116, y=446)
        time.sleep(1)
        pyautogui.click(x=116, y=446)
        time.sleep(5)
        # click send tip 10
        pyautogui.press('tab', presses=10)
        time.sleep(3)
        # Click Send
        pyautogui.press('enter')
        # click exit
        pyautogui.press('esc')
        tiploop += 1
    # CLicking loop to keep miner running
    start_time = time.time()
    seconds = 600
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        time.sleep(1)
        pyautogui.click(510, 106, duration=0.24)
        time.sleep(10)
        pyautogui.click(502, 465, duration=0.25)
        time.sleep(6)
        pyautogui.click(546, 66, duration=0.25)
        time.sleep(200)
        if elapsed_time > seconds:
            print("Finished loop")
            break

    # click EXIT
    pyautogui.click(491, 14, duration=0.25)
    print("FINSIHED TIPPING ", count1)
    # vpn change
    if count1 == 43:
        vpn_change()
    if count1 == 86:
        vpn_change()
    if count1 == 129:
        vpn_change()
    if count1 == 172:
        vpn_change()
    if count1 == 215:
        vpn_change()
    if count1 == 258:
        vpn_change()
    if count1 == 301:
        vpn_change()
    if count1 == 344:
        vpn_change()
    if count1 == 387:
        vpn_change()
    if count1 == 430:
        vpn_change()
    if count1 == 473:
        vpn_change()
    if count1 == 516:
        vpn_change()
    if count1 == 559:
        vpn_change()
    if count1 == 602:
        vpn_change()
    if count1 == 645:
        vpn_change()
    if count1 == 688:
        vpn_change()
    if count1 == 731:
        vpn_change()
    if count1 == 774:
        vpn_change()
    if count1 == 817:
        vpn_change()
    if count1 == 860:
        vpn_change()
    if count1 == 903:
        vpn_change()
    if count1 == 946:
        vpn_change()
    if count1 == 989:
        vpn_change()
    print("FINSIHED TIPPING ", count1)

    count1 += 1

from screen_search import *
import pyautogui
import time
import os
pyautogui.FAILSAFE = False
time.sleep(3)
print("Running Run.py")
print("Min All Windows")
pyautogui.hotkey("win", "m")
time.sleep(5)
# Start first anchor window
print("Opening Anchor Window")
start1 = r'cmd /c start "" /b "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"'
os.system(start1)
time.sleep(3)
print("Looking for restore")
restore = Search('Restore.png')
pos = restore.imagesearch()
if pos[0] != -1:
    clk = pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click(clk)
# Max Window
print("Maxing Window")
time.sleep(4)
fw1 = pyautogui.getActiveWindow()
fw1.maximize()
time.sleep(3)
# Click Minimize
print("Clicking Minimize")
pyautogui.click(910, 12)
# Start Main Loop
print("Starting Main Loop")
count4 = 2
while count4 < 1100:
    print("Runing Number" + str(count))
    start = r'cmd /c start "" /b "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe" --profile-directory="Profile "'
    b = count
    os.system(start + str(b))
    time.sleep(6)
    time.sleep(1)
    # Looking for restore
    print("looking for restore")
    restore = Search('Restore.png')
    pos = restore.imagesearch()
    # If Found CLick Restore
    if pos[0] != -1:
        clk = pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click(clk)
    # Max Window
    print("Maxing Window")
    time.sleep(4)
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(3)
    # click triangle
    print("clicking triangle")
    pyautogui.click(823, 49, duration=0.23)
    time.sleep(3)
    # Click Join Rewards
    pyautogui.click(552, 378, duration=0.23)
    time.sleep(4)
    pyautogui.click(553, 345, duration=0.25)
    time.sleep(4)
    # Click browser url bar
    time.sleep(3)
    # click Search Bar
    pyautogui.click(303, 46, duration=0.26)
    pyautogui.press('backspace')
    time.sleep(2)
    pyautogui.typewrite("www.iamdecarlo.com")
    time.sleep(10)
    pyautogui.press('enter')
    # pyautogui.click(912, 6, duration=0.26)
    time.sleep(6)
    print('ran', count)
    pyautogui.click(1002, 6)
    time.sleep(3)
    count4 += 1
# Open Window to Run Clicking loop on
pyautogui.hotkey('win', 'm')
time.sleep(10)
print("Opening window for clicking loop")
start2 = r'cmd /c start "" /b "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"'
os.system(start2)
time.sleep(10)
fw2 = pyautogui.getActiveWindow()
fw2.maximize()
time.sleep(10)
pyautogui.hotkey('win', 'left')
# Run Clicking Loop
time.sleep(3)
pyautogui.click(254, 58)
pyautogui.press('backspace')
time.sleep(2)
pyautogui.typewrite('www.ebay.com')
time.sleep(3)
pyautogui.press('enter')
print("running clicking loop...")
count5 = 1
while count5 < 1000:
    time.sleep(1)
    pyautogui.click(510, 106, duration=0.24)
    time.sleep(10)
    pyautogui.click(502, 465, duration=0.25)
    time.sleep(6)
    pyautogui.click(546, 66, duration=0.25)
    time.sleep(200)
