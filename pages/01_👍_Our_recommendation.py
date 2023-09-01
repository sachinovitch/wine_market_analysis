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

st.subheader("\n👍Here are our top 10 hightlights, where we select wines with "
             +"the highest ratings and more than 1000 ratings counts.")
presentation("queries/highlights10_apporoach1.sql")

st.subheader("\n👍Have a marketing budget? Here we select the 5 countries "
             + "with the cheapeast but good quality wines (ratings higher than 4.2)")
presentation("queries/country_with_budgets.sql")

st.subheader("\n👍Fancy some Cabernet Sauvignon? Here some options we "
             + "recommend for you.")
presentation("queries/cabernet.sql")
