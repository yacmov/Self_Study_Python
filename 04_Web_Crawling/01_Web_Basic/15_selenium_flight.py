from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window() # 창 최대화

url = "https://www.google.com/travel/flights?hl=ko"
driver.get(url) 

import time
T_sec = 1
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input').click()
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="ow81"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[3]/div[5]/div[6]/div/div[1]').click()
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="ow81"]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div[3]/div/div[1]').click()
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="ow81"]/div[2]/div/div[3]/div[3]/div/button/span').click()
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="i23"]/div[4]/div/div/div[1]/div/div/input').click()
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="c5"]/div[2]/div[1]/div').click()
time.sleep(T_sec)
driver.find_element(By.XPATH, '//*[@id="c2"]/div[2]/div[1]').click()

input()