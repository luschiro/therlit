import streamlit as st
from streamlit_ace import st_ace

file_path = 'databases/JUN92d.bs'  # Replace with the pa
with open(file_path, 'r') as file:
    db_value = file.read()
st.title("Database Editor")
st.write("#### edit your database")
st_ace(value=db_value,theme='dracula',height=780)
