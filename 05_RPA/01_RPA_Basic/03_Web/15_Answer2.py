import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# url 접속
driver.get('https://www.w3schools.com/')

# learn html 클릭
driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# 상단 메뉴 중 HOW TO 클릭
driver.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()

# 좌축 메뉴 중 Contact Form 메뉴 클릭
# a[숫자] 숫자 대신에 text()= 를 이용하여 텍스트를 비교할수 있다. 
driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 일치하는 것
# driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click() # 포함하는 것

# 입력란에 아래 값 입력

#  First Name : 나도
#  Last Name : 코딩
#  Country : Canada
#  Subject : 퀴즈 완료하였습니다.
#  * 위 값들은 변수로 미리 저장해 두세요
firstName = "나도"
lastName = "코딩"
Country = "Canada"
subject = "퀴즈를 완료하였습니다."

driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys(firstName)
driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys(lastName)
driver.find_element(By.XPATH, '//*[@id="country"]/option[text()=""{}"]'.format(Country)).click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)

elem = driver.find_element(By.LINK_TEXT, 'Submit')
elem.click()

# 6. 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
# 7. 5초 대기 후 브라우저 종료

driver.quit()

print("프로그램 완료")