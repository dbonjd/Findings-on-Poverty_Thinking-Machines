import matplotlib.pyplot as plt

# Given data set of high school football players
data = [350, 400, 450, 320, 550, 600, 450, 350, 500, 450, 350, 550]

# Generate y-axis labels (months of the year)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create horizontal bar plot with conditional color
colors = ['red' if d < 450 else 'green' for d in data]
plt.bar(months, data, color=colors)

# Add labels and title
plt.xlabel('Months in a Year')
plt.ylabel('Estimated Number of Customers')
plt.title("KickNation's Demand Forecast within a year")

# Display graph
plt.show()