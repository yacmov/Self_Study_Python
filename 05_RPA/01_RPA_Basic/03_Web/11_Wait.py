# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get('https://flight.naver.com/flights/')


# # 가는날 클릭
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
# time.sleep(1)

# # 가는 날짜 클릭
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button/b')
# time.sleep(1)
# elem.click()

# # 오는 날짜 클릭
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/button/b')
# time.sleep(1)
# elem.click()
# browser.execute_script('window.scrollTo(0,0)')

# # 도착 클릭
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i')
# time.sleep(1)
# elem.click()
# browser.execute_script('window.scrollTo(0,0)')

# time.sleep(1)
# # 국내 클릭
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]')
# time.sleep(1)
# elem.click()
# # browser.execute_script('window.scrollTo(0,0)')

# # 도시 클릭
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]/span/i[1]')
# time.sleep(1)
# elem.click()
# # browser.execute_script('window.scrollTo(0,0)')

# # 항공권 클릭
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span')
# time.sleep(1)
# elem.click()

# # time.sleep(10)
# try:
#     element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[1]/div[1]/div/div[2]')))
# except:
#     print("실패했어요")

# # try:
# #     elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[3]/div[2]/div/button')))
# # except:
# #     print("실패했어요")

# # 첫번째 결과 출력
# # elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[1]/div[1]/div/div[2]')
# # print(elem.text)


# time.sleep (5)
# browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://secure.flightcentre.com.au/2M3Zvdmo/results")
try:
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "results-screen")))
    # title_is # 타이틀이 같을때
    # title_contains # 타이틀을 포함할때
    # presence_of_element_located # 지정한 주소를 찾았을때 
    # visibility_of_element_located
    # visibility_of
    # presence_of_all_elements_located
    # text_to_be_present_in_element
    # text_to_be_present_in_element_value
    # frame_to_be_available_and_switch_to_it
    # invisibility_of_element_located
    # element_to_be_clickable
    # staleness_of
    # element_to_be_selected
    # element_located_to_be_selected
    # element_selection_state_to_be
    # element_located_selection_state_to_be
    # alert_is_present

    print(element.text)
except:
    print("실패 하였습니다.")
finally:
    driver.quit()