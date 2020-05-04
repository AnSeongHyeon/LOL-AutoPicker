import pyautogui
import time
# import cv2

position = input("Please enter the position you want: ")
if len(position) > 10:
    print("Please enter position within 10 characters")
    exit(1)

champion = input("Please enter the champion you want: ")
if len(champion) > 10:
    print("Please enter champion within 10 characters")
    exit(1)

while True:
    # champion
    while True:
        try:
            location = pyautogui.locateCenterOnScreen("images/champion/"+champion+".png",confidence=0.9)
            if location is not None:
                break
            time.sleep(0.01)    
        except OSError:
            print("없는 챔피언입니다.")
            exit(1)
    pyautogui.click(location)
    # position
    while True:
        location = pyautogui.locateCenterOnScreen("images/chat_window.png",confidence=0.8)
        if location is not None:
            break
    pyautogui.click(location)
    for i in range(10):
        pyautogui.write(position)
        pyautogui.press("enter")
    # ready
    while True:
        location = pyautogui.locateCenterOnScreen("images/ready_button.png",confidence=0.8)
        if location is not None:
            break
    pyautogui.click(location)