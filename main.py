import pyautogui
import time
import keyboard

def start_typing():
    time.sleep(5)

    with open("typing", "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                pyautogui.typewrite(word, interval=0.10)
                pyautogui.press("space")
                time.sleep(1)

            pyautogui.press("enter")


keyboard.add_hotkey("F7", start_typing)

# Wait for the hotkey to be pressed
keyboard.wait("esc")
