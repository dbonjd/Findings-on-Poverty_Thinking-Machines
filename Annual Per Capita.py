import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a pandas DataFrame
data = pd.read_csv('C:/Users/Bon/OneDrive/Desktop/TM_ExamRepo/povstat_processed.csv')

# plot a scatter plot to show the relationship between two variables
plt.scatter(data['Annual Per Capita Poverty Threshold(in Pesos)'], data['value'])

# add labels and a title to the plot
plt.xlabel('Annual Per Capita Poverty Threshold(in Pesos) ')
plt.ylabel('value(in Pesos)')
plt.title('Relationship between Annual Per Capity Poverty Threshold and value(in Pesos)')

# display the plot
plt.show()