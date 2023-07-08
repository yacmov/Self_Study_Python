import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 22,16 53,166,242 #35A6F2

pixel = pyautogui.pixel(22, 16)
print(pixel)


p = pyautogui.pixelMatchesColor(22, 16, (53,166,242))
print(p)