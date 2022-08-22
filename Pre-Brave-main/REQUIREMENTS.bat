@echo off

:start
cls

set python_ver=36

python ./get-pip.py
pip install --upgrade pip
cd \
cd \python%python_ver%\Scripts\
pip install xlrd
pip install XlsxWriter
pip install pandas
pip install pyautogui
pip install screen_search
pip install keyboard
pip install pillow
pip install pytesseract
pip install torch
pip install requests
pip install pysimplegui
cd /d %~dp0
pip install -r requirements.txt

pause
exit
