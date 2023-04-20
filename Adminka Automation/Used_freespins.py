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
user_name = 'narek.meloyan'
password = '!QAZ2wsx#EDC'
main_link = 'https://admindigitainnew.totogaming.am/#/login'
login_path = '//*[@id="mat-input-0"]'
password_path = '//*[@id="mat-input-1"]'
login_button = '/html/body/app-root/app-layouts/app-login-layout/div[2]/app-login/mat-card/div[2]/form/div[4]/button/span'
reports_button = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav/div/app-navigation-menu/ul/div[15]/a/span[2]'
internet_players_button = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav/div/app-navigation-menu/ul/div[15]/ul/div[4]/a/span[2]'
report_by_freespins = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav/div/app-navigation-menu/ul/div[15]/ul/div[4]/ul/div[2]/a/span[2]'
partner_name = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[1]/app-filter/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'
totogaming_option = '/html/body/div[4]/div[2]/div/div/div/mat-option[2]/span'
background_exit = '/html/body/div[4]/div[1]'
date_select = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[1]/app-filter/div/div[2]/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div'
custom = '/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span'
date_input = '//*[@id="ej2-datetimepicker_0_input"]'
show_result = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[1]/app-filter/div/div[2]/div/button[2]/span'
cell = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[1]/number-cell/div'
export_button = '/html/body/div[4]/div/div/context-menu-content/div/ul/li[1]/a'
unused_filter_open = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[1]/div/div[1]/div[2]/div/div/div[13]/header-cell/div/div[2]/button/span/mat-icon'
unused_freespin_is_equal = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[4]/div/div/number-filter-cell/mat-card/mat-card-content/mat-form-field[1]/div/div[1]/div/mat-select/div/div[1]/span/span'
unused_freespin_is_less_or_equal = '/html/body/div[4]/div[2]/div/div/div/mat-option[4]/span'
less_or_equal_input = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[4]/div/div/number-filter-cell/mat-card/mat-card-content/div[1]/mat-form-field/div/div[1]/div/input'
filter_less_or_equal = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[4]/div/div/number-filter-cell/mat-card/mat-card-actions/button[2]/span'
open_less_or_equal_filter = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[1]/div/div[1]/div[2]/div/div/div[13]/header-cell/div/div[2]/button/span/mat-icon'
clear_filter = '/html/body/app-root/app-layouts/app-platform-layout/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/app-report-by-free-spins/div/div[2]/div[1]/mat-sidenav-container/mat-sidenav-content/div/ag-grid-angular/div/div[4]/div/div/number-filter-cell/mat-card/mat-card-actions/button[1]/span'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def load_data(date, max_unused=None):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if max_unused is None:
        max_unused = 500
    folder_path = "C:/Users/narek.meloyan/Downloads/"
    files_path = os.path.join(folder_path, '*csv')
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    last_file = 'no file'
    if len(files) > 0:
        last_file = files[0]
    driver.get(main_link)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_path))).send_keys(user_name)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_path))).send_keys(password)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button))).click()
    time.sleep(3)
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
    time.sleep(3)
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

    frame = pd.read_csv(last_file_new, skiprows=2, low_memory=False)

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
    from_date = df_1.iloc[0, 0]
    from_date = from_date[10:26]
    from_date = datetime.strptime(from_date, "%d.%m.%Y %H:%M")
    day = from_date.strftime('%m-%d')
    from_date = from_date.strftime("%Y/%m/%d %H:%M")

    until_date = df_1.iloc[0, 1]
    until_date = until_date[11:27]
    until_date = datetime.strptime(until_date, "%d.%m.%Y %H:%M")
    until_date = until_date.strftime("%Y/%m/%d %H:%M")
    date = from_date + ' - ' + until_date

    df_2 = pd.read_csv(f, skiprows=2)
    max_num = max(df_2['FreeSpinCount'])

    statuses = load_data(date, max_num)
    df_2 = df_2[['Id', 'PlayerId', 'UniqueId', 'FreeSpinName', 'Original Provider', 'ProductName', 'FreeSpinCount', 'UsedFreeSpinCount', 'UnusedFreeSpinCount', 'ProvisionDate', "Campaign ID"]]
    statuses = statuses[['Id', 'PlayerFreeSpinStatus', 'UsedFreeSpinCount', 'UnusedFreeSpinCount', 'SumOfWin', 'LastUpdateTime']]


    statuses['LastUpdateTime'] = statuses['LastUpdateTime'].str[:10]
    statuses['LastUpdateTime'] = pd.to_datetime(statuses['LastUpdateTime'], format='%d.%m.%Y')
    statuses['LastUpdateTime'] = statuses['LastUpdateTime'].dt.date

    df_2['ProvisionDate'] = df_2['ProvisionDate'].str[:10]
    df_2['ProvisionDate'] = pd.to_datetime(df_2['ProvisionDate'], format='%d.%m.%Y')
    df_2['ProvisionDate'] = df_2['ProvisionDate'].dt.date


    CAMPAIGN_ID = df_2['Campaign ID'][0]
    final_frame = pd.merge(df_2, statuses, on='Id')
    final_frame.to_excel(f'Z:/Daily Personal Campaigns/Unused Freespins - Artur B/reults from Narek/Result_{CAMPAIGN_ID}.xlsx', index=False)


folder_path = "Z:/Daily Personal Campaigns/Unused Freespins - Artur B/reults from Narek/"

# Get a list of all Excel files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Initialize an empty DataFrame to store the results
all_data = pd.DataFrame()

# Loop through each file and append it to the DataFrame
for file in file_list:
    # Read the Excel file into a DataFrame
    data = pd.read_excel(os.path.join(folder_path, file))

    # Append the data to the all_data DataFrame
    all_data = all_data.append(data, ignore_index=True)
