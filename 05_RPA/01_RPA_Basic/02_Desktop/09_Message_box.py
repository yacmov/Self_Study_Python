import pyautogui
# print("곧 시작합니다...")
# pyautogui.countdown(3)
# print("자동화 시작")

# pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") # 확인 버튼만 있는 팝업
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
# print(result)
# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
# print(result)
result = pyautogui.password("암호를 입력하세요") # 암호 입력
print(result)

# more information 
# https://pyautogui.readthedocs.io/en/latest/