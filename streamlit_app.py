import streamlit
import pandas

streamlit.title('New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega-3 and Blueberry Oatmeal')
streamlit.text('Kale and Spinach Smoothie')
streamlit.text('Hard-boiled Cage-free egg')
streamlit.text('Avocado Toast')

streamlit.header('Build Your Own Fruit Smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
