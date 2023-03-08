import streamlit
import pandas
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from mytable")
my_data_rows = my_cur.fetchall()
fruit_choice1 = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice1)
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

streamlit.title("Shivali Naik")
