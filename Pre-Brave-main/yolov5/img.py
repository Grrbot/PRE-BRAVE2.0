import pyautogui
import time
count = 1
while count < 5000:
    
    print("running Number" + str(count))
    time.sleep(3)
    pyautogui.click(557, 324)
    time.sleep(3)
    im = pyautogui.screenshot(r'capimg\capimg'+ str(count) + '.png', region=(612,269, 312, 308))
    time.sleep(1)
    pyautogui.click(522, 585)

    count += 1
