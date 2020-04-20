import pyautogui

location = pyautogui.locateCenterOnScreen("lol_start.png")
pyautogui.click(location)

while True:
    location = pyautogui.locateCenterOnScreen("game_start.png")
    if type(location) != type(None):
        pyautogui.click(location)
        break
while True:
    location = pyautogui.locateCenterOnScreen("ok_btn.png")
    if type(location) != type(None):
        pyautogui.click(location)
        pyautogui.click(location[0],location[1]-100)
        break
while True:
    location = pyautogui.locateCenterOnScreen("search_btn.png")
    if type(location) != type(None):
        pyautogui.click(location)
        break
while True:
    location = pyautogui.locateCenterOnScreen("surak_btn.png")
    if type(location) != type(None):
        pyautogui.click(location)
        break

# print(location)
# while True:
#     location = pyautogui.locateCenterOnScreen("lol_start.png")
#     print(location)
    # if type(location) != type(None):
    #     pyautogui.click(location)
    

