from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from webdrivermanager.chrome import ChromeDriverManager
import os
import glob

# Set up Selenium options
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

# Set up the driver
driver = webdriver.Chrome(options=options)

# Load the page
url = "https://www.list.am/am/user/622659?c=60&pg=1"
driver.get(url)

# Wait for the content to load
time.sleep(5)

# Find all content divs
content_divs = driver.find_elements_by_class_name("contentr")

# Scrape the title, price, and description from each content div
data = []
for content_div in content_divs:
    # Get the title
    title_div = content_div.find_element_by_class_name("l")
    title = title_div.text.strip()

    # Get the price (if it exists)
    try:
        price_div = content_div.find_element_by_class_name("p")
        price = price_div.text.strip()
    except:
        price = "no price"

    # Get the description (if it exists)
    try:
        description_div = content_div.find_element_by_class_name("at")
        description = description_div.text.strip()
        # Decode the description
        decoded_description = description.encode('latin-1').decode('unicode_escape')
    except:
        description = ""
        decoded_description = ""

    # Add the data to the list
    data.append({"title": title, "price": price, "description": decoded_description})

# Close the driver
driver.quit()

# Convert the data to a DataFrame
import pandas as pd

df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
# df.to_csv("data.csv", index=False)
