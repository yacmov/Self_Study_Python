import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때가지 2초 대기
pyautogui.sleep(2)
window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판이 한개만 띄워져 있다고 가정함

if window.isMaximized == False:
    window.maximize() # 최대화 하기


paint_text = pyautogui.locateOnScreen("paint_text.png")
if paint_text:
    pyautogui.click(paint_text)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
pyautogui.click(200,400, duration=0.5)
# btn_brush = pyautogui.locateOnScreen("btn_brush.png")
# pyautogui.click(btn_brush.left - 200, btn_brush.top +200)
# 상대 좌표로 찾아가기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 프로그램 종료
pyautogui.sleep(5) # 5초 대기
window.close() # 종료 창 띄우기
pyautogui.sleep(0.5)
pyautogui.press("n") # 종료 단축키


