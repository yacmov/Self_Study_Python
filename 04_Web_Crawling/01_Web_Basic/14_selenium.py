from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. 네이버 이동
driver.get('http://www.naver.com/')

# 2. 로그인 버튼 클릭
elem = driver.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
elem.click()

# 3. id, pw 입력 
driver.find_element(By.ID, 'id').send_keys("naver_id")
driver.find_element(By.ID, 'pw').send_keys("password")

# 4. 로그인 버튼 클릭
driver.find_element(By.ID, "log.login").click()

# 5. id 를 새로 입력
time.sleep(3)
driver.find_element(By.ID, 'id').clear()
driver.find_element(By.ID, 'id').send_keys('my_id')

# 6. html 정보 출력
print(driver.page_source)

# 7. 브라우저 종료
# driver.close() # 현재 탭만 종료
driver.quit() # 전체 브라우저 종료



