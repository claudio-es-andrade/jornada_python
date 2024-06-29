import mysql.connector

# Create a MySQL connection
client = mysql.connector.connect(
    user='root',
    password='NovoRoot!@12',
    host='localhost',
    database='trends_db'
)

# Use the trends_db database
cursor = client.cursor()
cursor.execute("USE trends_db;")

# Now you can execute SQL queries against this database
cursor.execute("SELECT * FROM trends")
results = cursor.fetchall()

print(results)
