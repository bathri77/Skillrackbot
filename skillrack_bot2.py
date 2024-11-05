import pyautogui
import time

time.sleep(1)

for line in open("typing", "r"):
    pyautogui.typewrite(line, interval=0.1)  # Add a delay of 0.1 seconds between each character
    time.sleep(2)  # Add a delay of 2 seconds between each line
    pyautogui.press("enter")
