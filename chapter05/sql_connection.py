import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv(".env")

# ^ loading .env is only necessary on PyCharm.
# In other situations, Pipenv load them for you

usr = os.getenv("SQL_USR")
pwd = os.environ.get("SQL_PWD")

connection = mysql.connector.connect(host='localhost',
                                     database="cats_base",
                                     user=usr,
                                     password=pwd)

print(connection)  # No error == active connection!

# Test connection

query = "SELECT VERSION(), CURRENT_DATE;"

cursor = connection.cursor()
cursor.execute(query)
records = cursor.fetchall()  # `fetchall` will return a list of records.

print(records)  # For this query, there is only one row.


