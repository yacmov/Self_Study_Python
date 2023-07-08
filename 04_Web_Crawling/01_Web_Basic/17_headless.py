from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # Background runsize

driver = webdriver.Chrome(options=options)