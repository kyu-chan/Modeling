from selenium import webdriver
import pandas as pd
import numpy as np
import os
import glob
from openpyxl import load_workbook


#### investing.com 로그인
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.investing.com')

sel="#userAccount > div > a.login.bold"
ui = driver.find_element_by_css_selector(sel)
ui.click()

sel="#loginFormUser_email"
ui = driver.find_element_by_css_selector(sel)
ui.send_keys("iopoh0203@gmail.com")

sel="#loginForm_password"
ui = driver.find_element_by_css_selector(sel)
ui.send_keys("Dhrbcks950203!")

sel="#signup > a"
ui = driver.find_element_by_css_selector(sel)
ui.click()
###로그인 완료

driver.get('https://www.investing.com/indices')
### pair 166이 s&p 500
sel = "#pair_name_166 > a"
ui = driver.find_element_by_css_selector(sel)
ui.click()

url= driver.current_url + "-historical-data"
driver.get(url)

### #column-content > div.float_lang_base_2.downloadDataWrap > div > a 다운로드 링크
sel="#column-content > div.float_lang_base_2.downloadDataWrap > div > a"
ui = driver.find_element_by_css_selector(sel)
ui.click()


###위까지가 자동다운로드

