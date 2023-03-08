import streamlit
import pandas
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from mytable")
my_data_rows = my_cur.fetchall()
streamlit.dataframe(my_data_rows)

streamlit.title("Shivali Naik")



