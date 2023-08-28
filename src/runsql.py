#! /usr/bin/python3
import sqlite3

class SQL():
    def __init__(self):
        self._connection = sqlite3.connect("database/vivino.db")
        self._cursor = self._connection.cursor()

    def run_fromfile(self, path):
        with open(path, "r") as file:
            q = file.read().replace('\n', ' ')
        self._cursor.execute(q)
        return self._cursor.fetchall()

    def run_fromtext(self, query):
        self._cursor.execute(query)
        return self._cursor.fetchall()

    def cnn_close(self):
        self._connection.close()
