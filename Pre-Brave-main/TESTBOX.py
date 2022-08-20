
from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
import time
import random

from Capatcha import CPATCHA
def GIF():
    oldtime = time.time()
    gif_list = ['gifs/giphy.gif','gifs/suckit.gif','gifs/3.gif','gifs/4.gif','gifs/5.gif']
    gif = random.choice(gif_list)
    bear = r'img/' + str(gif)
    layout = [[sg.Image(key='-IMAGE-')]]
    window = sg.Window('SUCK IT PRE', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)
    sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(bear))]
    interframe_duration = Image.open(bear).info['duration']

    while True:
        for frame in sequence:
            event, values = window.read(timeout=interframe_duration)
            # check
            if time.time() - oldtime > 5:
                print ("EYYY")
                exit()            
            time.sleep(.08)
            window['-IMAGE-'].update(data=frame)
        time.sleep(3)
        break

#GIF()
CPATCHA()