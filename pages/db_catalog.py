import streamlit as st
import os
from os.path import isfile, join

st.title("Database Catalog")
st.write("#### current databases available for reference")

DATABASE_DIR = "databases"
list_databases = [f for f in os.listdir(DATABASE_DIR) if isfile(join(DATABASE_DIR, f))]

db1, db2, db3 = st.tabs([list_databases[0],list_databases[1],list_databases[2]])

with db1:
    with open(os.path.join('databases',list_databases[0]), 'r') as d:
        database_text = d.read()
        d.close()
        st.code(database_text, language=None)
with db2:
    with open(os.path.join('databases',list_databases[1]), 'r') as d:
        database_text = d.read()
        d.close()
        st.code(database_text, language=None)
with db3:
    with open(os.path.join('databases',list_databases[2]), 'r') as d:
        database_text = d.read()
        d.close()
        st.code(database_text, language=None)