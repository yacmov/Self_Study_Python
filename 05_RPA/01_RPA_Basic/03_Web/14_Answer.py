import time
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/')
driver.maximize_window()

time.sleep(1)

# 화면 중간 learn html 클릭
driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(1)

# 화면 상단 메뉴 중 how to 클릭
driver.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()
time.sleep(1)

# 좌축 메뉴 중 contact form 메뉴 클릭
driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()
time.sleep(1)


# First Name
firstName = pyperclip.copy("나도")
time.sleep(1)
elem = driver.find_element(By.XPATH, '//*[@id="fname"]')
time.sleep(1)
elem.click()
pyautogui.hotkey('ctrl', 'v')

# last Name
driver.execute_script('window.scrollTo(0,100)')
lastName = pyperclip.copy("코딩")
time.sleep(1)
elem = driver.find_element(By.XPATH, '//*[@id="lname"]')
time.sleep(1)
elem.click()
pyautogui.hotkey('ctrl', 'v')

# Country 
time.sleep(1)
elem = driver.find_element(By.XPATH, '//*[@id="country"]/option[text()="Canada"]')
elem.click()


# subject
time.sleep(1)
firstName = pyperclip.copy("퀴즈 완료 하였습니다.")
elem = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea')
elem.click()
pyautogui.hotkey('ctrl', 'v')


time.sleep(5)
driver.execute_script('window.scrollTo(0,200)')
# submit 버튼 클릭
elem = driver.find_element(By.LINK_TEXT, 'Submit')
elem.click()

time.sleep(5)
driver.quit()
print("프로그램 완료")