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
    time.sleep(6)
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
    search = Search("restore.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        clk = pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click(clk, duration=0.4)
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

    # Click Claim
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
    time.sleep(20)

    # FIND TOTAL BAT GENERATED FOR MONTH
    batimg = pyautogui.screenshot(region=(258, 438, 57, 34))
    time.sleep(2)
    batimg = cv2.cvtColor(np.array(batimg), cv2.COLOR_RGB2BGR)
    cv2.imwrite("battotal.png", batimg)
    img = cv2.imread("battotal.png")
    bat = pytesseract.image_to_string(img, lang='eng')
    time.sleep(3)

    # PRINT BAT TOTAL PER MINER
    print('TOATAL BAT FOR MONTH', bat)

    # CLICK OK
    ok = pyautogui.locateCenterOnScreen('ok.png')
    pyautogui.click(ok, duration=0.25)
    time.sleep(3)

    # PRINT TO CSV FILE
    csvRow = [bat + "BAT", "wallet" + str(count), currentMonth]
    csvfile = "BATTOTAL.csv"
    with open(csvfile, "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(csvRow)
    time.sleep(2)
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
