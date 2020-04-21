import pyautogui
# import cv2

contents = "wr"

while True:
    # chat
    while True:
        location = pyautogui.locateCenterOnScreen("images/chat_window.png")
        if type(location) != type(None):
            break
    pyautogui.click(location)
    for i in range(10):
        pyautogui.write(contents)
        pyautogui.press("enter")

    # elise
    while True:
        location = pyautogui.locateCenterOnScreen("images/elise_icon.png")
        if type(location) != type(None):
            break
    pyautogui.click(location)

    # ready
    while True:
        location = pyautogui.locateCenterOnScreen("images/ready_button.png")
        if type(location) != type(None):
            break
    pyautogui.click(location)