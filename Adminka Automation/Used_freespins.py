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

load_dotenv()
user_name = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
main_link = os.environ.get('MAIN_PAGE')
login_path = os.environ.get('LOGIN_PATH')
password_path = os.environ.get('PASSWORD_PATH')
login_button = os.environ.get('LOGIN_BUTTON')
reports_button = os.environ.get('REPORTS_BUTTON')
internet_players_button = os.environ.get('INTERNET_PLAYERS_BUTTON')
report_by_freespins = os.environ.get('REPORT_BY_FREE_SPINS')
partner_name = os.environ.get('PARTNER_NAME')
totogaming_option = os.environ.get('TOTOGAMING')
background_exit = os.environ.get('BACKGROUND_EXIT')
date_select = os.environ.get('DATE_SLICER')
custom = os.environ.get('CUSTOM_SELECT')
date_input = os.environ.get('DATETIME_INPUT')
used_filter = os.environ.get('USED_FREESPIN_FILTER')
used_filter_equal = os.environ.get('USED_FREESPIN_IS_EQUAL')
used_filter_greater = os.environ.get('USED_FREESPIN_IS_GREATER')
used_filter_input_1 = os.environ.get('USER_FREESPIN_IS_GREATER_INPUT')
used_select_filter = os.environ.get('AND_FILTER')
used_select_less = os.environ.get('AND_IS_LESS')
used_less_input = os.environ.get('LESS_INPUT')
filter_button = os.environ.get('FILTER_BUTTON')
show_result = os.environ.get('show_result')
cell = os.environ.get('ARBITRARY_CELL')
export_button = os.environ.get('EXPORT_BUTTON')
clear_button = os.environ.get('CLEAR_BUTTON')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

folder_path = "C:/Users/narek.meloyan/Downloads/"
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
last_file = files[0]

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(main_link)
driver.maximize_window()
login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_path))).send_keys(user_name)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_path))).send_keys(password)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, reports_button))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, internet_players_button))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, report_by_freespins))).click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, partner_name))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, totogaming_option))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, background_exit))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, date_select))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, custom))).click()

date_input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, date_input)))
date_input_field.send_keys(Keys.CONTROL + "a")
date_input_field.send_keys(Keys.DELETE)
date_input_field.send_keys('2023/02/06 00:00 - 2023/02/12 23:59')
time.sleep(3)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_filter))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_filter_equal))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_filter_greater))).click()
time.sleep(1)

greater_than_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_filter_input_1)))
greater_than_input.send_keys(Keys.CONTROL + "a")
greater_than_input.send_keys(Keys.DELETE)
greater_than_input.send_keys(0)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_select_filter))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_select_less))).click()

less_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, used_less_input)))
less_input.send_keys(Keys.CONTROL + "a")
less_input.send_keys(Keys.DELETE)
less_input.send_keys(10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, filter_button))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, show_result))).click()

cell_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, cell)))
actions = ActionChains(driver)
actions.context_click(cell_button).perform()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, export_button))).click()
time.sleep(20)

status = True
while status:
    files_path = os.path.join(folder_path, '*csv')
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    last_file_new = files[0]
    if last_file_new != last_file:
        status = False
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[1]/div/div[1]/div[2]/div/div/div[12]/header-cell/div/div[2]/button/span/mat-icon'))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, clear_button))).click()

frame = pd.read_csv(last_file_new, skiprows=2)
print(frame.head())
