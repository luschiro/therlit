import streamlit as st

def main():
    
    # setup pages
    home = st.Page("pagination/home.py")
    runner_page = st.Page("theriak_runner/runner.py")
    db_catalog_page = st.Page("pagination/db_catalog.py")

    # setup navigation and run
    pg = st.navigation([home,runner_page,db_catalog_page])
    pg.run()

if __name__ == "__main__":
    main()