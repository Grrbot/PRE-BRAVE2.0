def run2():
    # DELETE FOLDER SO I CAN PULL IMAGES
    print("RUNNING SECOND TIME ")
    print(" OPENING FOLDER TO DELETE")
    # checking whether folder exists or not
    files2 = 'runs/detect/exp'
    try:
        shutil.rmtree(files2)
    except OSError as e:
        print("Error: %s : %s" % (files2, e.strerror))

    # IMG TO TEXT TO GET TARGET TEXT

    # Take Screen Shot of TARGET
    print('TAKING SCREENSHOT OF TARGET TEXT')
    img2 = pyautogui.screenshot(region=(375, 146, 224, 57))
    time.sleep(3)

    # CONVERT IMAGE TO CV2 READABLE
    print('CONVERTING IMAGE')
    image2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)

    # SAVE IMAGE TO FILE NAMED TARGET.PNG
    print('Saving image to target.png')
    cv2.imwrite("target.png", image2)
    # READ IMAGE WITH CV2
    print('READING IMAGE')
    img2 = cv2.imread("target.png")

    # GET TEXT FROM TARGET.PNG TO SEE WHAT TO DRAG TO
    print('EXTRACTING TEXT FROM IMAGE')
    text2 = pytesseract.image_to_string(img2, lang='eng')

    # CHECK IF TEXT WAS FOUND
    print('FOUND : \"', text2, '\"')
    train2 = "train"
    truck2 = "truck"
    airplane2 = "airplane"
    bike2 = "bike"
    motorcycle2 = "motorcycle"
    bus2 = "motorbus"
    seaplane2 = "seaplane"
    boat2 = "boat"
    # car = "car"

    # Wait for images to show
    print("waiting for images to show")
    time.sleep(3)
    print("Taking ScreenShot For Cropping")

    # SCREEN SHOT OF IMAGES
    capimg2 = pyautogui.screenshot("img.png")
    time.sleep(3)
    results = model(capimg2)
    crops = results.crop(save=True)

    # RUN CLICK CMD BASED ON TARGET VARIABLE
    if train2 in text2:
        print("LOOKING FOR TRAINS TO CROP")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/train/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if truck2 in text2:
        print("LOOKING FOR TRUCKS")
        print("POINTING AI TO FIND ALL TRUCK IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/trucks/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if airplane2 in text2:
        print("LOOKING FOR AIRPLAINS")
        print("POINTING AI TO FIND ALL AIRPLANE IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/plane/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if bike2 in text2:
        print("LOOKING FOR BIKES")
        print("POINTING AI TO FIND ALL BIKE IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/bike/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if motorcycle2 in text2:
        print("LOOKING FOR MOTORCYCLES")
        print("POINTING AI TO FIND ALL MOTORCYCLES IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/motorcyle/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if bus2 in text2:
        print("LOOKING FOR BUSSES")
        print("POINTING AI TO FIND ALL BUS IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/bus/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if seaplane2 in text2:
        print("LOOKING FOR SEAPLANES")
        print("POINTING AI TO FIND ALL SEAPLANES IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/seaplane/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
    if boat2 in text2:
        print("LOOKING FOR SEAPLANES")
        print("POINTING AI TO FIND ALL BOAT IMAGES")
        # CREATE LIST OF CROPPED IMAGES TO MAKE INTO VAR FOR PYAUTOGUI
        dir_path2 = 'runs/detect/exp/crops/boat/'
        # Iterate directory
        res2 = os.listdir(dir_path2)
        print(res2)
        for x2 in range(len(res2)):
            print(res2[x2])
            # CLICK THE IMAGES FOUND IN FILE
            var22 = dir_path2 + res2[x2]
            var12 = pyautogui.locateOnScreen(var22)
            pyautogui.moveTo(var12)
            print("LOOKING FOR CROPPED IMAGE")
            print(var12)
            print("CLICKING IMAGE")
            pyautogui.click()
