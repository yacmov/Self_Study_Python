import pyautogui
pyautogui.sleep(3) # 3 초 대기 ( 초단위 )
# print(pyautogui.position())

# pyautogui.click(64,17, duration=1) # (64, 17) 좌표를 마우스 클릭
# pyautogui.click() # 좌표가 들어가지 않으면 현재 위치를 클릭함
# pyautogui.mouseDown() 
# pyautogui.mouseUp()


# pyautogui.doubleClick()
# pyautogui.click(clicks=500) # 총 몇번 클릭을 할것인지 정의해줄수 있다.


# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()
# pyautogui.moveTo(1113, 349)
# pyautogui.drag(100, 0, duration =0.25) 
# pyautogui.dragto(1514, 349, duration =0.25)
# 너무 빠른 동작으로 이동할경우 duration 을 이용하여 사람이 하는것처럼 만들수 있다.

pyautogui.scroll(300) # 양수이면 위 방향으로 300 만큼 스크롤
pyautogui.scroll(-300) # 음수이면 아래 방향으로 300 만큼 스크롤
