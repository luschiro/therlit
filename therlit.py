import streamlit as st
from pytheriak import wrapper

import matplotlib.pyplot as plt
import pandas as pd



# from src import utils

# config
st.title("Welcome to Therlit!")
st.write("#### a simple app to run Theriak.")
st.write("""this will be a description... """)

# input
with st.container(border=True):
    bulk = st.text_input("bulk composition", "SI(0.852)TI(0.009)AL(0.451)MG(0.154)MN(0.004)K(0.069)NA(0.033)CA(0.021)FE(0.162)F3(0.02)H(0.135)O(?)")
    database_choice = st.selectbox(label="database", options=["tcds55_p07_cord.bs"])
    c1, c2 = st.columns(2)
    with c1:
        pressure = st.text_input("Pressure", "5500")
    with c2:
        temperature = st.text_input("Temperature", "800")
    
calc = st.button("run")


# processing when button
if(calc):

    # rock, element_list = tr.run_theriak(pressure,temperature,bulk,database_choice,utils.THERIAK_DIR)

    BUILD_DIR = 'theriak'    
    theriak = wrapper.TherCaller(programs_dir=BUILD_DIR,
                                 database=database_choice,
                                 theriak_version="v2023.01.02beta")
    rock, element_list = theriak.minimisation(pressure, temperature, bulk)



    print('---------------\n')
    print(rock.bulk_composition_moles )    
    
    # results

    col1, col2 = st.columns(2)
    # bulk and chemistry
    with col1:
        with st.container(border=True):
            st.write("**BULK INFORMATION**")
            st.write("**_bcm_** - bulk composition moles")
            st.write("**_bcmp_** - bulk composition moles percent")
            
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
            st.write("**_vmol%_** - molar volume percent")

            min_names, min_vols = [], []
            for mineral in rock.mineral_assemblage:
                min_names.append(mineral.name)
                min_vols.append(mineral.vol_percent)
            df_percent = pd.DataFrame({
                'phases': min_names,
                'vmol%': min_vols
            })
            st.write(df_percent)
    
    # pie chart with vol%
    fig, ax = plt.subplots()
    ax.pie(x=min_vols,labels=min_names)
    st.pyplot(fig)