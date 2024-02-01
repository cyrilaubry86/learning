import pyautogui
import time
import random

while True:
    pyautogui.moveRel(random.randint(-200, 200), random.randint(-200, 200))
    time.sleep(2)