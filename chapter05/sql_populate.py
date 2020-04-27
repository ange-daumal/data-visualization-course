import os
import random

import mysql.connector
from dotenv import load_dotenv

load_dotenv(".env")

# ^ loading .env is only necessary on PyCharm.
# In other situations, Pipenv load them for you

usr = os.getenv("SQL_USR")
pwd = os.environ.get("SQL_PWD")

print(usr, pwd)
connection = mysql.connector.connect(host='localhost',
                                     database="cats_base",
                                     user=usr,
                                     password=pwd)

cursor = connection.cursor()

possible_values = {
    "Names": ["Tigrou", "Caramel", "Felix", "Simba", "Garfield", "Berlioz",
              "Moustache", "Moufassa", "Azraël", "Sylvestre", "Oggy", "Rouky"],
    "EyeColor": ["cyan", "lime", "black", "sienna", "gold"],
    "CoatColor": ["orange", "black"],
}

nb_cats = 10

for i in range(nb_cats):
    cat_sample = []
    for col, values in possible_values.items():
        cat_sample.append(random.choice(values))
    query = 'INSERT INTO cats VALUES (NULL, %s, %s, %s);'
    cursor.execute(query, cat_sample)  # Parameterized Query
    print(cat_sample)

print()

query = "SELECT * FROM cats;"

cursor = connection.cursor()
cursor.execute(query)

print(cursor.fetchall())

cursor.close()
