import os

import requests
import mysql.connector
from dotenv import load_dotenv

import pandas as pd

load_dotenv(".env")

# ^ loading .env is only necessary on PyCharm.
# In other situations, Pipenv load them for you

usr = os.getenv("SQL_USR")
pwd = os.getenv("SQL_PWD")

tmdb_key = os.getenv("tmdb_key")
tmdb_api = os.getenv("tmdb_api")

# You may want to edit that
database = "cats_base"
table_name = "cats"

connection = mysql.connector.connect(host='localhost',
                                     database=database,
                                     user=usr,
                                     password=pwd)

cursor = connection.cursor()


def create_table(table_name):
    cursor.execute(f""" DROP TABLE IF EXISTS {table_name} ;""")

    query = f"""
        CREATE TABLE {table_name} (  
        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,  
        title VARCHAR(255) NOT NULL,   
        description TEXT NOT NULL
        );
        """

    cursor.execute(query)


def parse_imdb_csv(table_name, filepath):
    data = pd.read_csv(filepath)

    for row in data.itertuples():
        if "cat" in row.Title or "cat" in row.Description:
            query = f"INSERT INTO {table_name} (title, description) VALUES (%s,%s)"
            cursor.execute(query, (row.Title, row.Description))

    # Commit your changes.
    connection.commit()


def tmdb_pages2df(keywords="cat"):
    headers = {
        "Authorization": f"Client-ID {tmdb_key}"
    }

    total_pages = -1  # We don't know this number yet.

    # Prepare a DataFrame to save parsed rows.

    df = pd.DataFrame(columns=["title", "description"])

    def parse_page(i=1):
        query = f"{tmdb_api}search/movie" \
            f"?api_key={tmdb_key}" \
            f"&query={keywords}" \
            f"&page={i}"

        response = requests.get(query, headers=headers)

        if response.status_code != 200:
            print("*** Error with request:", response.text)
            return

        data = response.json()
        total_pages = data['total_pages']  # Update the number of total_pages.

        for film in data['results']:
            df.loc[len(df)] = [film['title'], film['overview']]

    parse_page(1)

    if total_pages < -1:
        for i in range(2, total_pages + 1):
            parse_page(i)

    return df


def tmdb_df2table(df):
    for i, row in df.iterrows():
        query = f"INSERT INTO {table_name} (title, description) VALUES (%s,%s)"
        cursor.execute(query, (row['title'], row['description']))


if __name__ == '__main__':
    # Prepare the database
    create_table(table_name)

    # Parse the IMDB data (.csv) -- Change the location if needed
    parse_imdb_csv(table_name, "chapter05_solutions/IMDB-Movie-Data.csv")

    # Get the TMBD data (.json)
    df = tmdb_pages2df()  # .json => df
    tmdb_df2table(df)  # df => into database

    connection.commit()

cursor.close()
