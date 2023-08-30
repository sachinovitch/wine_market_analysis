import streamlit as st
import pandas as pd
import sqlite3

#load database

connection = sqlite3.connect("database/vivino.db")
cursor = connection.cursor()

# function to take the sidebar input and form an query
def get_query(min_price,max_price, rating_min,rating_max,country_list):
    if len(country_list) > 1:
        country_list_tuple = tuple(country_list)
        query = f"""
        SELECT vintages.name AS wine, vintages.price_euros AS Price, vintages.ratings_average AS Rating, countries.name AS Country 
        FROM vintages
JOIN wines ON vintages.wine_id = wines.id
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE  (vintages.price_euros BETWEEN {min_price} AND {max_price})
    AND (vintages.ratings_average BETWEEN {rating_min} AND {rating_max})
    AND (countries.name IN {country_list_tuple})
ORDER BY vintages.ratings_average DESC
LIMIT 10 
"""
        
    elif len(country_list)==1 :
        countryname = country_list[0]
        query = f"""
        SELECT vintages.name AS wine, vintages.price_euros AS Price, vintages.ratings_average AS Rating, countries.name AS Country 
        FROM vintages
JOIN wines ON vintages.wine_id = wines.id
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code

WHERE countries.name = '{countryname}'
    AND (vintages.price_euros BETWEEN {min_price} AND {max_price})
    AND (vintages.ratings_average BETWEEN {rating_min} AND {rating_max})
    
ORDER BY vintages.ratings_average DESC
LIMIT 10 
"""
    else:
        query = f"""
        SELECT vintages.name AS wine, vintages.price_euros AS Price, vintages.ratings_average AS Rating, countries.name AS Country 
        FROM vintages
JOIN wines ON vintages.wine_id = wines.id
JOIN regions ON wines.region_id = regions.id
JOIN countries ON regions.country_code = countries.code
WHERE  (vintages.price_euros BETWEEN {min_price} AND {max_price})
    AND (vintages.ratings_average BETWEEN {rating_min} AND {rating_max})
ORDER BY vintages.ratings_average DESC
LIMIT 10 
"""
    return query

def get_country():
    """This function retuns a list of the countries for the multi select box for the sidebar"""
    df = pd.read_csv("database/csv/countries.csv")
    country_list = df["name"].unique()
    return country_list

# Here below is the code to define the main page
st.title("Find the wine you like!")

# Here below is the code to define the side bar
# slider for price
st.sidebar.text('\n\n\n')
st.sidebar.markdown("**Select the wine in your mind:** 👇")
st.sidebar.write("(No, no wine over 150 euro.)")
price = st.sidebar.slider('Price range', 0.0, 150.0, (10.0, 50.0),step = 1.0)

# slider for rankings
ratings = st.sidebar.slider('Ratings', 4.0, 5.0,(4.1, 5.0),step = 0.1)

# multiselect country
countrylist = get_country()
country = st.sidebar.multiselect("Country",countrylist)


#show me the wine button
show_button = st.sidebar.button("Show me wine")
    
if show_button:
    min_price = price[0]
    max_price = price[1]
    rating_min = ratings[0]
    rating_max = ratings[1]
    if country:
        country_list = country
    else: country_list = []
    # st.write(f"{min_price},{max_price},{rating_min},{rating_max},{country_list}")
    q = get_query(min_price,max_price, rating_min,rating_max,country_list)
    
    data = pd.read_sql_query(q,connection)
    st.dataframe(data)




