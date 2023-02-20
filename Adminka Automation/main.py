import pandas as pd
import os
import glob


folder_path = 'Z:/Daily Personal Campaigns/Unused Freespins - Artur B/raw data/'


# use glob to get all the csv files
# in the folder
path = folder_path
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_csv(f, nrows=1)

    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

    # print the content
    print('Content:')
    print(df.head())
    print()
