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
