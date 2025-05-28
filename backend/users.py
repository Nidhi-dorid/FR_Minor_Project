import sqlite3

# Connect to your SQLite database file
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to fetch all users
cursor.execute("SELECT * FROM users")

# Fetch all rows from the result
rows = cursor.fetchall()

# Print all the users
print("ID | Username | Email | Password")
print("----------------------------------")
for row in rows:
    print(row)

# Close the connection
conn.close()

