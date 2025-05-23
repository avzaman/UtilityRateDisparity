#This script will be used for getting uszips data and saving as csv for home machine parsing
#This script needs to be ran on obi in order to use mysql-connector library
import csv
import mysql.connector

# Define the database connection parameters
connection = mysql.connector.connect(
    host='*******',
    user='*******',
    password='*******',
    database='*******'
)

# Create a cursor object
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM Income"
cursor.execute(query)

# Fetch column names
columns = [desc[0] for desc in cursor.description]

# Fetch and store the query results
rows = cursor.fetchall()

# Close cursor and connection
cursor.close()
connection.close()

# Write the results to a CSV file
csv_file = 'cleanincome.csv'
with open(csv_file, 'w') as f:
    writer = csv.writer(f)
    
    # Write column names to the CSV file
    writer.writerow(columns)
    
    # Write rows to the CSV file
    writer.writerows(rows)
