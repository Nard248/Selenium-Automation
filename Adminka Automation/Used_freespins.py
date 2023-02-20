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


def load_data(date, max_unused=None):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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


files_path = 'Z:/Daily Personal Campaigns/Unused Freespins - Artur B/raw data/'

csv_files = glob.glob(os.path.join(files_path, "*.csv"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df_1 = pd.read_csv(f, nrows=1)
    from_date = df_1.index[0]
    from_date = from_date[10:26]
    from_date = datetime.strptime(from_date, "%d.%m.%Y %H:%M")
    until_date = df_1.iloc[0, 0]
    until_date = until_date[11:27]
    until_date = datetime.strptime(until_date, "%d.%m.%Y %H:%M")
    day = from_date.strftime('%m-%d')
    from_date = str(from_date).replace('-', '/')
    until_date = str(until_date).replace('-', '/')
    date = from_date[:len(from_date) - 3] + ' - ' + until_date[:len(until_date)-3]
    print(date)
    df_2 = pd.read_csv(f, skiprows=2)
    max_num = max(df_2['FreeSpinCount'])
    statuses = load_data(date, max_num)
    final_frame = pd.merge(df_2, statuses, on='Id')
    final_frame['Notif Date'] = from_date
    print(final_frame)
    final_frame.to_excel(f'Result_{day}.xlsx')