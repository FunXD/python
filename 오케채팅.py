
import os, threading, pyautogui,time, keyboard
from datetime import datetime
from datetime import timedelta
def start_check():
    pyautogui.click(135, 665, button='left', clicks=1, interval=1)
    keyboard.write('20405 박준하 1타')
    keyboard.press_and_release('enter')

timee = input("몇시몇분 ㄱ?")
now = time.localtime()
now_times = ("%02d:%02d" % (now.tm_hour, now.tm_min))
tom_times = (timee)
HM = '%H:%M'
time_dif = datetime.strptime(tom_times, HM) - datetime.strptime(now_times, HM)
if time_dif.days < 0:
    time_dif = timedelta(days=0,seconds=time_dif.seconds, microseconds=time_dif.microseconds)
hours,mins,_ = str(time_dif).split(":")
result_min = int(hours) * 3600 + int(mins) * 60
threading.Timer(result_min, start_check).start()
