import os
import glob
import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime



def function():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://app.powerbi.com/home?cmpid=pbi-glob-head-snn-signin')
    driver.maximize_window()
    email = '//*[@id="email"]'
    time.sleep(20)
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, email))).send_keys(
        'narek.meloyan@digitain.com')
    submit_button = '//*[@id="submitBtn"]'
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, submit_button))).click()
    workspaces = '//*[@id="leftNavPane"]/div/div/tri-workspace-switcher/tri-navbar-label-item/button/div/tri-svg-icon[2]'
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, workspaces))).click()

    crm = '/html/body/div[2]/div[3]/div/tri-workspace-flyout/div/cdk-virtual-scroll-viewport/div[1]/tri-workspace-button[2]/button'
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, crm))).click()

    search = '//*[@id="mat-input-0"]'
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, search))).send_keys('High')
    time.sleep(20)
    march_highs = '//*[@id="artifactContentView"]/div[1]/div[9]/div[2]/span/a'

    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, march_highs))).click()

    time.sleep(10)
    time.sleep(10)


for i in range(57):
    function()
