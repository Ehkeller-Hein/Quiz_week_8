import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
data = pd.read_csv('climate.csv')  # Replace 'your_data.csv' with the actual CSV file path

# Assuming your CSV file has columns named 'Date' and 'Temperature'
# You can modify these column names based on your data
years = data['Year']
cO2 = data['CO2']
temperatures = data['Temperature']

# Create a figure and plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

plt.plot(years, temperatures, marker='o', linestyle='-', color='b')
plt.title('ClimateData')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.grid(True)


# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()





