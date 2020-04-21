import pyautogui

location = None
position = input("Please enter the position you want: ")
champion = input("Please enter the champion you want: ")
if len(position) > 10 and len(champion) >10:
    print("Please enter 10 word")
    exit(1)

while True:

    # champion
    while True:
        location = pyautogui.locateCenterOnScreen("images/champion/elise.png")
        if location is not None:
            break
    pyautogui.click(location)

    # position
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