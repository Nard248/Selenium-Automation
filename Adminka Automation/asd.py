import glob
import os
import pandas as pd

folder_path = "C:/Users/narek.meloyan/Downloads/"
files_path = os.path.join(folder_path, '*csv')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
print(files[0])
a = pd.read_csv(files[0], skiprows=2)
print(a.head())
