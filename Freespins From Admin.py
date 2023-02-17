import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import datetime
from os import listdir
from os.path import isdir
import pandas as pd
from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains

username = 'gegham.harutyunyan'#input('Input adminka login: ').strip()
password = '!QAZ2wsx#EDC'#input('Input adminka pass: ').strip()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.get('https://admindigitainnew.totogaming.am/#/login')

driver.maximize_window()


driver.find_element("xpath", '//*[@id="mat-input-0"]').send_keys(username)

driver.find_element("xpath", '//*[@id="mat-input-1"]').send_keys(password)

driver.find_element("xpath", '/html/body/app-root/app-layouts/app-login-layout/div[2]/app-login/mat-card/div[2]/form/div[4]/button/span').click()
time.sleep(3)
driver.find_element("xpath", '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav/div/app-navigation-menu/ul/div[16]/a/span[2]').click()

driver.find_element("xpath", '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav/div/app-navigation-menu/ul/div[16]/ul/div[4]/a/span[2]').click()

driver.find_element("xpath", '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav/div/app-navigation-menu/ul/div[16]/ul/div[4]/ul/div[2]/a/span[2]').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,'/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[1]/app-filter/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]'))).click()

driver.find_element("xpath", '//*[@id="mat-option-41"]/span').click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[1]/app-filter/div/div[2]/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span'))).click()
time.sleep(3)

datetime = driver.find_element("xpath", '//*[@id="ej2-datetimepicker_0_input"]')
datetime.send_keys(Keys.CONTROL + "a")
datetime.send_keys(Keys.DELETE)
datetime.send_keys('2023/02/16 00:00 - 2023/02/17 23:59')
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[1]/app-filter/div/div[2]/div/button[2]/span'))).click()
time.sleep(6)
clickable = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[1]/number-cell/div')))
actions = ActionChains(driver)
actions.context_click(clickable).perform()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/context-menu-content/div/ul/li[1]/a'))).click()
time.sleep(15)



