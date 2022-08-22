from screen_search import *
import pyautogui
import time
# LOGIC FOR BRAVE USERS
# START LOGIC FOR NEW BROSWER USERS BAT OPEN IN NEW TAB
def newbrowseruser():

    # CHANGING OPEN BROWSER TO NEW TAB
    print("CLICKING Browser HAMBURGER MENU")
    pyautogui.click(999, 53)
    print("Moving down to Settings options")
    time.sleep(5)
    pyautogui.press('up', presses=4)
    pyautogui.press('enter')
    time.sleep(4)   
    print("Clicking new tab start") 
    pyautogui.click(586, 416)
    # CHANGING REWARDS TO ON AND 10 MAX
    print("CLICKING Browser HAMBURGER MENU")
    pyautogui.click(999, 53)
    print("moving down to rewards options")
    time.sleep(5)
    pyautogui.press('down', presses=5)
    pyautogui.press('enter')
    time.sleep(4)
    # MOVE WINDOW TO MAKE SURE START IS GO
    print("MOVING WINDOW TO START POSITION")
    pyautogui.press('up', presses=15)
    time.sleep(2)
    pyautogui.press('up', presses=15)
    rewardson = pyautogui.locateCenterOnScreen("img/startrewards.png")
    time.sleep(2)
    if rewardson:
        pyautogui.moveTo(rewardson)
        print("CLICKING REWARDS ON ")
        pyautogui.click()
        time.sleep(3)
        skip2 = pyautogui.locateCenterOnScreen("img/skip2.png")
        if skip2:
            print("Clicking Skip Tour")
            pyautogui.moveTo(skip2)
            pyautogui.click()
        time.sleep(3)
        done = pyautogui.locateCenterOnScreen("img/done.png")
        time.sleep(1)
        if done:
            print("Clicking done")
            pyautogui.moveTo(done)
            pyautogui.click()
        time.sleep(4)
        print("MOVING WINDOW TO LEFT 4 CLICKS ")
        pyautogui.press('right', presses=4)
        time.sleep(2)
        print("MOVING WINDOW DOWN 10 CLICKS")
        pyautogui.press('down', presses=10)
        print("Looking for autocontrib")
        off = pyautogui.locateCenterOnScreen("img/autocontoff.png")
        print(off)
        if off:
            print("Autocontrib ALREADY OFF")
        else:
            time.sleep(2)
            print("CLICKING AUTO CONTRIB OFF")
            pyautogui.click(913, 366)
        # OPEN NEW TAB TO MINE TAB ADDS
        print("Opening new tab to mine tab adds")
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)
        cnt = 1
        while cnt < 8:
                print('refreshing window')
                pyautogui.press('f5')
                time.sleep(5)
                cnt += 1


    else:
        # REFRESH PAGE JUST IN CASE
        print("refresh page")
        pyautogui.press('f5')
        print("making sure page is at the top")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'home')
        time.sleep(2)
        print("Moving Window to start Position")
        pyautogui.press('left', presses=10)
        time.sleep(2)
        print("Moving window to the left")
        pyautogui.press('right', presses=4)
        print("Checking if rewards are on")
        time.sleep(3)
        rewardsoff = pyautogui.locateCenterOnScreen("img/rewardsoff.png")
        if rewardsoff:
            time.sleep(2)
            print("Rewards currently Off Turning On")
            pyautogui.moveTo(rewardsoff)
            time.sleep(1)
            pyautogui.click()
            print("Turned adds on ....... GET THAT COIN!")
        else:
            print("Rewards Already On AYY")
            # make Sure 10 max is set
            tenmax = pyautogui.locateCenterOnScreen("img/10max.png")
            if tenmax:
                print("making ten max")
                time.sleep(1)
                pyautogui.click(tenmax)
                time.sleep(3)
                # CLICK MENU DOWN BUTTON
                print("clicking menu down button")
                pyautogui.click(919, 430)
                time.sleep(3)
                # CLICKING 10 Max
                print("clicking 10 max")
                pyautogui.click(713, 695)

        print("Moving window to see Autocontrib")
        time.sleep(3)
        pyautogui.press('down', presses=10)
        time.sleep(2)
        autocontribon = pyautogui.locateCenterOnScreen("img/autoconton.png")
        if autocontribon:
            print("Found auto contrib on, turning off!")
            pyautogui.moveTo(autocontribon)
            time.sleep(1)
            pyautogui.click()
            print("Turned it off,... Suck it Brave")
        else:
            print("Auto Contrib Already Off GOOD ! ")
        # OPEN NEW TAB TO MINE TAB ADDS
        print("Opening new tab to mine tab adds")
        pyautogui.hotkey('ctrl', 't')
        time.sleep(3)
        print("CLICKING SO BJ CAN EAGLE EYE")
        pyautogui.click(1014, 697, clicks=6, interval=0.6)
        cnt = 1
        while cnt < 6:
                print('refreshing window')
                pyautogui.press('f5')
                time.sleep(3)
                cnt += 1
