import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
            
browser.switch_to.frame('iframeResult')

## cars 에 해당하는 element 를 찾고, 드롭다운 내부에 있는 4 번째 옵션을 선택함
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
## option[1] : 첫번째 항목
## option[2] : 두번째 항목
## option[3] : 세번째 항목
## option[4] : 네번째 항목

# elem.click()

## 옵션값에서 숫자대신 텍스트를 적으면 텍스트를 찾아서 선택한다.
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
time.sleep(3)

# 부분적으로 AU만 포함해도 선택한다.
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(5)