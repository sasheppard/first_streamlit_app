import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega-3 and Blueberry Oatmeal')
streamlit.text('Kale and Spinach Smoothie')
streamlit.text('Hard-boiled Cage-free egg')
streamlit.text('Avocado Toast')

streamlit.header('Build Your Own Fruit Smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New section to display the response from the API call
streamlit.header('Fruityvice Fruit Advice!')
# question the user about fruit
fruit_choice = streamlit.text_input('What fruit do you want to know about?', 'Apple')
streamlit.write('The user entered', fruit_choice)

# import requests

# adding the user's friut choice to the call
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response.json())

# take the json string from response and make it look better
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the output
streamlit.dataframe(fruityvice_normalized)

# for troubleshooting
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# fruit_load_list is a table in PC_RIVERY_DB in Snowflake
my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
# fetchone should return banana
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.text("The fruit load list contains:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# ask to choose another fruit
add_my_fruit = streamlit.text_input('What fruit do you want to add?', 'Apple')
streamlit.write('Thanks for adding', add_my_fruit) 

# adding the next line to demostrate control flow. It gets fired each time a text box changes
my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")

