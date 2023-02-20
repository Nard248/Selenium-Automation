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
show_result = os.environ.get('show_result')
cell = os.environ.get('ARBITRARY_CELL')
export_button = os.environ.get('EXPORT_BUTTON')
unused_filter_open = os.environ.get('UNUSED_FREESPIN_FILTER_1')
unused_freespin_is_equal = os.environ.get('UNUSED_FREESPIN_IS_EQUAL')
unused_freespin_is_less_or_equal = os.environ.get('UNUSED_FREESPIN_IS_LESS_OR_EQUAL')
less_or_equal_input = os.environ.get('UNUSED_FREESPIN_IS_LESS_OR_EQUAL_INPUT')
filter_less_or_equal = os.environ.get('UNUSED_FREESPIN_FILTER_2')
open_less_or_equal_filter = os.environ.get('UNUSED_FREESPIN_CLEAR_FILTER_OPEN')
clear_filter = os.environ.get('UNUSED_FREESPIN_CLEAR_FILTER')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def load_data(date, max_unused=None):
    if max_unused is None:
        max_unused = 500
    folder_path = "C:/Users/narek.meloyan/Downloads/"
    files_path = os.path.join(folder_path, '*csv')
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    last_file = files[0]

    driver.get(main_link)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_path))).send_keys(user_name)
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
    date_input_field.send_keys(date)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, unused_filter_open))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, unused_freespin_is_equal))).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, unused_freespin_is_less_or_equal))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, less_or_equal_input))).send_keys(
        max_unused)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, filter_less_or_equal))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, show_result))).click()

    cell_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, cell)))
    actions = ActionChains(driver)
    actions.context_click(cell_button).perform()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, export_button))).click()
    time.sleep(25)

    status = True
    while status:
        files_path = os.path.join(folder_path, '*csv')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        last_file_new = files[0]
        if last_file_new != last_file:
            status = False

    frame = pd.read_csv(last_file_new, skiprows=2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, open_less_or_equal_filter))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, clear_filter))).click()
    driver.close()
    return frame


frame = load_data('2023/02/06 00:00 - 2023/02/12 23:59', 500)
print(frame.head())
print(frame.shape)
