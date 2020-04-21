import pyautogui

location = None
position = input("Please enter the position you want: ")

while True:

    # elise
    while True:
        location = pyautogui.locateCenterOnScreen("images/elise_icon.png")
        if location is not None:
            break
    pyautogui.click(location)

    # chat
    while True:
        location = pyautogui.locateCenterOnScreen("images/chat_window.png")
        if location is not None:
            break
    pyautogui.click(location)
    for i in range(10):
        pyautogui.write(position)
        pyautogui.press("enter")
        
    # ready
    while True:
        location = pyautogui.locateCenterOnScreen("images/ready_button.png")
        if location is not None:
            break
    pyautogui.click(location)