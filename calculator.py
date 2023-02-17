import pandas as pd
import os

# specify the folder path where your Excel files are located
folder_path = "Z:\Analytics\Ani's Flow Analysis\\1st Step Lists"

# create an empty list to store the dataframes
dataframes = []

# loop through all the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is an Excel file
    if filename.endswith('.xlsx'):
        # read the Excel file into a dataframe
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)
        # add the dataframe to the list
        dataframes.append(df)

# concatenate all the dataframes into one dataframe
result = pd.concat(dataframes, axis=0, ignore_index=True)
print(result)