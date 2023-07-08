import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = driver.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보

elem = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/a')
elem.click()

# 브라우저 탭 정보 가져오기
# 탭간 이동은 핸들값을 사용한다
handles = driver.window_handles # 모든 핸들 정보를 가져옴
for handle in handles:
    print(handle) # 각 핸들 정보를 출력
    driver.switch_to.window(handle)
    print(driver.title) # 현재 핸들의 제목 값을 가져옴
    print()

# 선택된 브라우저 종료
print("현재 핸들 닫기")
driver.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
driver.switch_to.window(curr_handle)

print(driver.title)

# 브라우저 컨트롤이 가능한지 확인
driver.get('http://daum.net')

time.sleep(5)
driver.quit()