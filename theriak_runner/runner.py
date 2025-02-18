from pytheriak import wrapper
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("THERIAK runner")
st.write("#### just run it already..")

# input container
with st.container(border=True):
    bulk = st.text_input("bulk composition", 
                         "SI(0.852)TI(0.009)AL(0.451)MG(0.154)MN(0.004)K(0.069)NA(0.033)CA(0.021)FE(0.162)F3(0.02)H(0.135)O(?)")
    

    database_choices = ["JUN92d.bs",
                        "tcds55_p07_cord.bs",
                        "td-ds62-mb50-v07.txt","td-ds62-mp50-v05.txt","td-ds633-ef21-v03.txt","td-ds633-ef21-v03.txt"]
    database_choice = st.selectbox(label="database", options=database_choices)
    
    c1, c2 = st.columns(2)
    with c1: pressure = st.text_input("Pressure", "5500")
    with c2: temperature = st.text_input("Temperature", "800")
    
calc = st.button("run")


if(calc):

    # minimisation
    theriak = wrapper.TherCaller(programs_dir='theriak_runner',
                                 database=database_choice,
                                 theriak_version="v2023.01.02beta")
    rock, element_list = theriak.minimisation(pressure, temperature, bulk)

    # results
    with st.container(border=True):
        col1, col2 = st.columns(2) 
        
        with col1:
                st.write("**BULK INFORMATION**")
                df_meta = pd.DataFrame({
                    'elements': element_list,
                    'bcm':rock.bulk_composition_moles,
                    'bcmp':rock.bulk_composition_mol_percent
                })
                st.write(df_meta)
                st.write("**_bcmp_** - bulk composition moles percent")
                st.write("**_bcm_** - bulk composition moles")
        
        with col2:
                st.write("**MINERAL ASSEMBLAGE INFORMATION**")
                min_names, min_vols = [], []
                for mineral in rock.mineral_assemblage:
                    min_names.append(mineral.name)
                    min_vols.append(mineral.vol_percent)
                df_percent = pd.DataFrame({
                    'phases': min_names,
                    'vmol%': min_vols
                })
                st.write(df_percent)
                st.write("**_vmol%_** - molar volume percent")
    
    # pie chart with vol%
    fig, ax = plt.subplots()
    ax.pie(x=min_vols,labels=min_names)
    st.pyplot(fig)




# def run_theriak(P,T,bulk,dirr,db):
     
#      st.write("entered run_theriak")
#      st.write(P, T, bulk, dirr, db)
#      theriak = wrapper.TherCaller(programs_dir=dirr,
#                                  database=db,
#                                  theriak_version="v2023.01.02beta",
#                                  verbose=True)
#      st.write(theriak.theriak_exe)
#      rock, element_list = theriak.minimisation(P, T, bulk)

#      return rock, element_list