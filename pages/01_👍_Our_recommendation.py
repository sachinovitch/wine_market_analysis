import streamlit as st
import pandas as pd
import sqlite3

connection = sqlite3.connect("database/vivino.db")
cursor = connection.cursor()
def presentation(path):

    with open(path, "r") as file:
            q = file.read().replace('\n', ' ')
    df = pd.read_sql_query(q,connection)
    st.dataframe(df,hide_index=True)

st.title("Here are some of our recommendations!")

st.subheader("\n👍Here are our top 10 hight lights, where we select wines with the highest ratings, more than 1000 ratings counts.")
presentation("queries/highlights10_apporoach1.sql")

st.subheader("\n👍Having a marketing budget? Here we select the 5 countries with the lowest price for wine, yet with good quality (ratings higher than 4.2)")
presentation("queries/country_with_budgets.sql")

st.subheader("\n👍Fancy some Cabernet Sauvignon? Here's something similiar we would recommend you to give a try.")
presentation("queries/cabernet.sql")
