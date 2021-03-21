from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
### 다우존스 169,
#pair_178 > td.bold.left.noWrap.elp.plusIconTd > a
##pair_8859 > td.bold.left.noWrap.elp.plusIconTd > a
#cross_rates_container > table > tbody > tr:nth-child(1) > td.bold.left.plusIconTd.noWrap.elp > a
sel = "#realTimeStockMarkets > h2 > a"
ui = driver.find_element_by_css_selector(sel)
ui.click()
#cross_rates_container > table > tbody > tr:nth-child(1) > td.bold.left.plusIconTd.noWrap.elp > a
#cross_rates_container > table > tbody > tr:nth-child(2) > td.bold.left.plusIconTd.noWrap.elp > a
##마지막 #cross_rates_container > table > tbody > tr:nth-child(45) > td.bold.left.plusIconTd.noWrap.elp > a

###xpath sp5002 //*[@id="cross_rates_container"]/table/tbody/tr[2]/td[2]/a
###xpath 다우1 //*[@id="cross_rates_container"]/table/tbody/tr[1]/td[2]/a
###마지막 //*[@id="cross_rates_container"]/table/tbody/tr[45]/td[2]/a
id = "cross_rates_container"
xpath = f"//*[@id={id}]/table/tbody/tr[2]/td[2]/a"
href = driver.find_element(xpath)
driver.get(href.get_attribute('href'))

########### href를 쓸수 있는 다른 기술이 필요할 듯 지금으로선 수동다운로드 진행하겠음
'''
url= driver.current_url + "-historical-data"
driver.get(url)

### #column-content > div.float_lang_base_2.downloadDataWrap > div > a 다운로드 링크
sel="#column-content > div.float_lang_base_2.downloadDataWrap > div > a"
ui = driver.find_element_by_css_selector(sel)
ui.click()


###위까지가 자동다운로드
'''