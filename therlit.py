import streamlit as st
# import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
from pytheriak import wrapper
from pathlib import Path


# title
st.title("Welcome to Therlit!")
st.write("#### A simple app to run Theriak!")

# selections
with st.container(border=True):
    c1, c2 = st.columns(2)
    database_choice = st.selectbox(label="choose database", options=["tcds55_p07_cord.bs"])
    bulk = st.text_input("bulk composition", "SI(0.852)TI(0.009)AL(0.451)MG(0.154)MN(0.004)K(0.069)NA(0.033)CA(0.021)FE(0.162)F3(0.02)H(0.135)O(?)")

    with c1:
        temperature = st.text_input("Temperature", "550")
    with c2:
        pressure = st.text_input("Pressure", "7000")

calc = st.button("run")

if(calc):

    BUILD_DIR = 'theriak_only'
    st.write(BUILD_DIR)
    st.write(Path(BUILD_DIR))
    theriak = wrapper.TherCaller(programs_dir=BUILD_DIR,
                                 database=database_choice,
                                 theriak_version="v2023.01.02beta")
    rock, element_list = theriak.minimisation(pressure, temperature, bulk)

    print('---------------\n')
    print(rock.bulk_composition_moles )    
    

    col1, col2 = st.columns(2)

    # bulk and chemistry
    with col1:
        with st.container(border=True):
            st.write("**BULK INFORMATION**")
            df_meta = pd.DataFrame({
                'elements': element_list,
                'bcm':rock.bulk_composition_moles,
                'bcmp':rock.bulk_composition_mol_percent
            })
            st.write(df_meta)

    # mineral assemblage
    with col2:
        with st.container(border=True):
            st.write("**MINERAL ASSEMBLAGE INFORMATION**")
            # st.write(f"**Mineral Assemblage @ {rock.therin_PT}**")

            min_names, min_vols = [], []
            for mineral in rock.mineral_assemblage:
                min_names.append(mineral.name)
                min_vols.append(mineral.vol_percent)
                st.write(mineral.name, mineral.vol_percent)
     
    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(x=min_vols,labels=min_names)
    # ax.axis('equal')
    st.pyplot(fig)