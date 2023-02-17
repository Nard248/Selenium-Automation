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
users = result['CasinoID']
import pyodbc

cnx = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DWH;"
    "Database=dwOper;"
    "Trusted_Connection=yes;")

query = """
SELECT u.Base_UserID                                  AS CasinoID,
       SUM(p.Amount)                                  AS Amount
FROM Payment AS p
INNER JOIN VIEW_PlatformPartnerUsers_TotogamingAm AS u ON u.UserID = p.UserID
WHERE p.PaymentTypeID = 2
    AND p.PaymentStatusID = 8
    AND CAST(DATEADD(hour, -4, p.modify_date) AS DATE) >= '2023-01-01'
    AND CAST(DATEADD(hour, -4, p.modify_date) AS DATE) < CAST(GETDATE() AS DATE)
    AND u.PartnerID IN (237)
    AND p.SourceID = 2
GROUP BY u.Base_UserID
"""

deposit_data = pd.read_sql(query, cnx)
cnx.close()
deposit_data.head()

import numpy as np
Q1 = deposit_data['Amount'].quantile(0.25)
Q3 = deposit_data['Amount'].quantile(0.75)
IQR = Q3 - Q1

thresh = 1.5 * IQR

deposit_data['Outlier'] = np.where((deposit_data['Amount'] < (Q1 - thresh)) | (deposit_data['Amount'] > (Q3 + thresh)), True, False)
deposit_data
users = users.to_frame().merge(deposit_data, on='CasinoID')
users[users['Outlier'] == True]