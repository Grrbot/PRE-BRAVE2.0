from screen_search import *
import pyautogui
import time
import os
count = 1
time.sleep(3)
while count < 140:
    a = 'cmd /c  start "" /max /b "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --profile-directory="Profile '
    print("Running Start")
    # RUN REFERAL FOR presearchnode1@protonmail.com
    b = '" https://presearch.com/signup?rid=4171706'

    # START BROSWER
    start = a + str(15) + b
    os.system(start)
    time.sleep(5)
    fw = pyautogui.getActiveWindow()
    fw.maximize()
    time.sleep(3)
    print("Moving Window to The Right")
    pyautogui.hotkey('win', 'right')
    time.sleep(2)
    # SEARCH IF ALREADY LOGGED IN
    pyautogui.locateCenterOnScreen("")
    # CLICK JOIN
    join = pyautogui.locateCenterOnScreen("img/join.png")
    time.sleep(2)
    pyautogui.click(join)
    time.sleep(5)
    pyautogui.click(1822, 399)
    e = "presearchnode1+4bc"
    d = "@protonmail.com"
    email = e + str(count) + d
    pyautogui.typewrite(email, interval=0.02)
    time.sleep(4)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.typewrite("@Starwars2", interval=0)
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.typewrite("@Starwars2", interval=0)
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("tab", presses=2)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(8)

    # Search For Save LOGIN INFO
    search = Search("img/savelogin.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        clk = pyautogui.locateCenterOnScreen('img/savelogin.png')
        pyautogui.click(clk, duration=0.4)
        time.sleep(3)

    else:
        print("save not found")
        time.sleep(2)

    # Exit Current User
    pyautogui.click(2473, 119)
    time.sleep(4)
    pyautogui.click(2474, 346)


    # EXIT WINDOW
    pyautogui.hotkey("alt", "f4")
    pyautogui.sleep(2)
    print("Ran Number" + str(count))
    time.sleep(2)
    count += 1

