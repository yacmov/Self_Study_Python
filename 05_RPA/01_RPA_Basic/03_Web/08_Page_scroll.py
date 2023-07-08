from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://shopping.naver.com/home')

# 검색창을 찾고 바로 입력하도록 한줄에 입력도  가능함
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.send_keys('무선 마우스')
elem.send_keys(Keys.ENTER)


# 스크롤
# 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 768)') # 디스플레이 최대 해상도가 768 이므로 768를 입력했음 - 현재 모니터

# 화면 가장 아래로 이동함
# window 쓸때 s 조심하기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 마지막 페이지까지 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이에 변화가 없으면
        break #  반복문 탈출 (모든 스크롤 동작 완료)
    
    # 만약 같지 않으면 현재 높이를 이전 높이에 업데이트 시켜준다.
    prev_height = curr_height

# scrollTo 적을때 T 대문자 조심하기
browser.execute_script('window.scrollTo(0,0)')

time.sleep(5)