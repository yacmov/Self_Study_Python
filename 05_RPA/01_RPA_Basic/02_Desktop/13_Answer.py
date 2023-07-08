import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint", interval =0.1)
pyautogui.press("enter")

paint_max = None
while paint_max is None:
    paint_max = pyautogui.locateOnScreen("paint_maximize.png", confidence=0.9)

pyautogui.click(paint_max)

paint_text = None
while paint_text is None:
    paint_text = pyautogui.locateOnScreen("paint_text.png", confidence=0.9)

pyautogui.click(paint_text)

#125,355
# pyautogui.mouseInfo()
# pyautogui.sleep(3)
pyautogui.moveTo(125,355)
pyautogui.click()
pyperclip.copy("참 잘했어요")

pyautogui.hotkey("ctrl","v")


pyautogui.sleep(5)
paint_x = None
while paint_x is None:
    paint_x = pyautogui.locateOnScreen("paint_x.png", confidence=0.9)

pyautogui.click(paint_x)


paint_nosave = None
while paint_nosave is None:
    paint_nosave = pyautogui.locateOnScreen("paint_nosave.png", confidence=0.9)

pyautogui.click(paint_nosave)