import pandas as pd

# read the CSV file
data = pd.read_csv('C:/Users/Bon/OneDrive/Desktop/TM_ExamRepo/povstat_processed.csv')

# set the pandas display options to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# print the entire DataFrame
print(data)
