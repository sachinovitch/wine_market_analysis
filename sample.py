#! /usr/bin/python3
import src.runsql as runsql
import pandas as pd
import sqlite3

# saving tables from the database to csv
connection = sqlite3.connect("database/vivino.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabel_names = cursor.fetchall()
tabel_names = [table[0] for table in tabel_names]


for tabel in tabel_names:
    query = f"SELECT * FROM {tabel}"
    df = pd.read_sql_query(query, connection)
    csv_file = f'./database/csv/{tabel}.csv'
    df.to_csv(csv_file, index=False)