import time
import os
import pyperclip
import sys
recent_value = ""
D = time.strftime("%D")
r = time.strftime("%r")
from time import strftime
sys.path.append(os.path.abspath("SO_site-packages"))
while True:

    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value Changes: %s" % str(recent_value)[:20])
        with open("estimated.txt.txt", '+a') as output:
            try:

                output.write("%s\n\n" % str(tmp_value))

            except:
                output.write("----"+ D + "" + r+",------\n")
                output.write("%s\n\n" % str(tmp_value.encode('UTF-8')))
                output.write("-----------------\n\n\n")
    time.sleep(0.1)