import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a SQL query to fetch data from the database
cursor.execute('SELECT Year, CO2, Temperature FROM ClimateData')

# Fetch all the rows as a list of tuples
rows = cursor.fetchall()

# Close the database connection
conn.close()

# Define Python lists to store the values
column1_values = []
column2_values = []
column3_values = []

# Populate the Python lists with values from the database
for row in rows:
    column1_values.append(row[0])
    column2_values.append(row[1])
    column3_values.append(row[2])

# Now, column1_values and column2_values contain the values from the database
