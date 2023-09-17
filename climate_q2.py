import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
data = pd.read_csv('climate.csv')


years = data['Year']
cO2 = data['CO2']
temperatures = data['Temperature']

# Create a figure and plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

plt.plot(years, cO2, marker='o', linestyle='-', color='b')
plt.subplot(2, 1, 1)
plt.plot(years, cO2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temperatures, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()





