import pyautogui

# # 맥에선 안됨
# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표
# pyautogui.click(fw.left + 10, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("07")[0]

print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)
pyautogui.sleep(1)
if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화 하기

pyautogui.sleep(1)
if w.isMinimized == False: # 현재 최소화가 되지 않았다면
    w.minimize() # 최소화 하기

pyautogui.sleep(1)
w.restore()

w.close() # 윈도우 닫기