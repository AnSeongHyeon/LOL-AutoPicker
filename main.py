import pyautogui

location = pyautogui.locateCenterOnScreen("lol_start.png")
pyautogui.click(location)

while True:
    location = pyautogui.locateCenterOnScreen("game_start.png")
    if type(location) != type(None):
        pyautogui.click(location)
        break

# print(location)
# while True:
#     location = pyautogui.locateCenterOnScreen("lol_start.png")
#     print(location)
    # if type(location) != type(None):
    #     pyautogui.click(location)
    

