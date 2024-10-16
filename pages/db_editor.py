import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(layout="wide")

file_path = 'databases/JUN92d.bs'  # Replace with the pa
with open(file_path, 'r') as file:
    db_value = file.read()

c1, c2 = st.columns([1,3])

with c1:
    st.write("### Edit your database!")
with c2:
    st_ace(value=db_value,theme='dracula',height=500)