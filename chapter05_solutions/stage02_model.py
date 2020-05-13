import os
import pickle

import mysql.connector
import pandas as pd
from dotenv import load_dotenv
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

load_dotenv(".env")

usr = os.getenv("SQL_USR")
pwd = os.getenv("SQL_PWD")

database = "cats_base"
table_name = "cats"

model_path = "last_model.pickle"
vectorizer_path = "last_vectorizer.pickle"


def save_obj(obj, fpath):
    with open(fpath, 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(fpath):
    if os.path.exists(fpath):
        with open(fpath, 'rb') as f:
            return pickle.load(f)


def get_model():
    model = RandomForestClassifier(n_estimators=1000, random_state=0)
    return model


def preprocess(x: list, new_vectorizer: bool = True):
    vectorizer = load_obj(vectorizer_path)
    if new_vectorizer or not vectorizer:
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(x)
        save_obj(vectorizer, vectorizer_path)
    else:
        X = vectorizer.transform(x)
    return X


def train_model(model):
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user=usr,
                                         password=pwd)

    query = pd.read_sql_query(f"SELECT title, description FROM {table_name}",
                              connection)

    df = pd.DataFrame(query, columns=['title', 'description'])

    x, y = df.description, df.title
    X = preprocess(x)
    model.fit(X, y)

    # Save the trained model
    save_obj(model, model_path)

    return model


def predict(x: list) -> pd.ndarray:
    model = load_obj(model_path)
    if not model:
        model = train_model(get_model())

    X = preprocess(x, new_vectorizer=False)
    y_pred = model.predict(X)
    return y_pred


if __name__ == '__main__':
    train_model(get_model())
