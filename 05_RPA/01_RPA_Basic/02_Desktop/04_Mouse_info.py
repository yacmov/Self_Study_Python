import pyautogui
#pyautogui.mouseInfo() # mouseinfo app open
# pyautogui.FAILSAFE = False # 마우스 귀퉁이에 넣으면 멈추는 기능을 정지 시킨다
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

for i in range(10):
    pyautogui.move(100,100)
    # pyautogui.sleep(1)