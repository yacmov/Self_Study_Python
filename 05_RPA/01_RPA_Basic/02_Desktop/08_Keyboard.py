import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()
# pyautogui.write("12345")
# pyautogui.write("Nadocoding", interval=1)

# pyautogui.write(["t","e","s","left","left","right","l","enter"], interval= 0.25)
# Automate the boring stuff with Python - google search

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 땐다

# pyautogui.keyDown("ctrl") # ctrl 키를 누른 상태에서
# pyautogui.keyDown("a") # a 를 누르고
# pyautogui.keyUp("a") # a 를 땐다
# pyautogui.keyUp("ctrl") # ctrl 키를 땐다


# pyautogui.hotkey("ctrl", "alt", "shift", "a")
pyautogui.hotkey("ctrl", "a")



# 한글 처리하는 법
#pip install pyperclip - 파이썬용 클립보드 복사
import pyperclip
pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("너도코딩")

# 자동화 프로그램 종료
# win ctrl + alt + del
# mac : cmd + shift + option + q