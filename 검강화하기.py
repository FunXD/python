import pyautogui as pg
import time
from PIL import ImageGrab
import pynput


#try:
for i in range(100):
    screen = ImageGrab.grab()
    if screen.getpixel(pg.position(759, 757)) == (198, 122, 0):
        pg.click(1074,529)
    else:
        pg.click(1034,736)
#except keyboardinterrupt:
#    pass
