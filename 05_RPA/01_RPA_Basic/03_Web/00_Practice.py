from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import pyperclip


chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\yacmo\Desktop\Programing_Language\Python\99_Extra'})
firsttime = True
driver = webdriver.Chrome(options=chrome_options)
while(True):
    url = input()
    # url = ''
    pyautogui.click(50,50)
    elem = None
    driver.get(url)
    # for i in range(10):
    #     time.sleep(1)
    #     print(f"{i}s")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_player"]/div[2]/div[5]')))
    except:
        print("비디오 플레이 실패")
    driver.find_element(By.XPATH, '//*[@id="kt_player"]/div[2]/div[5]').click()
    driver.execute_script('window.scrollTo(0, 768)')

    time.sleep(10)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_player"]/div[2]/div[4]/div[1]')))
    except:
        print("스킵 실패")
    driver.find_element(By.XPATH, '//*[@id="kt_player"]/div[2]/div[4]/div[1]').click()


    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kt_player"]/div[2]/video')))
    except:
        print("비디오 찾기 실패")

    elem = driver.find_element(By.XPATH, '//*[@id="kt_player"]/div[2]/video')

    url = elem.get_attribute('src')
    text = elem.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/h1')
    pyperclip.copy(text.text)
    test2 = text.text

    driver.get(url)

    time.sleep(2)
    pyautogui.hotkey('ctrl','s')    
    time.sleep(2)
    # if firsttime == True:
    #     input()
    #     firsttime = False
    #     pyautogui.click(50,50)
    #     time.sleep(1)
    # text11 = 'C:/Users/yacmo/Desktop/Programing_Language/Python/99_Extra/'
    # pyautogui.write(text11)
    # pyperclip.copy()
    pyautogui.hotkey('ctrl','v')
    # pyperclip.copy("\\")
    # pyautogui.hotkey('ctrl','v')
    # pyperclip.copy(text.text)
    # pyautogui.hotkey('ctrl','v')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('enter')





    #     # title_is # 타이틀이 같을때
    #     # title_contains # 타이틀을 포함할때
    #     # presence_of_element_located # 지정한 주소를 찾았을때
    #     # visibility_of_element_located
    #     # visibility_of
    #     # presence_of_all_elements_located
    #     # text_to_be_present_in_element
    #     # text_to_be_present_in_element_value
    #     # frame_to_be_available_and_switch_to_it
    #     # invisibility_of_element_located
    #     # element_to_be_clickable
    #     # staleness_of
    #     # element_to_be_selected
    #     # element_located_to_be_selected
    #     # element_selection_state_to_be
    #     # element_located_selection_state_to_be
    #     # alert_is_present

    #     print(element.text)
    # except:
    #     print("실패 하였습니다.")
    print('{} : 다운로드 시작'.format(test2))