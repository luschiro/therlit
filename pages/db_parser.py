import pandas as pd
import streamlit as st
# databases
# file_path = 'pages/td-ds62-mb50-v07.txt'  # Replace with the path to your .bs file
# file_path = 'pages/JUN92d.bs'  # Replace with the path to your .bs file
file_path = 'pages/tcds55_p07_cord.bs'  # Replace with the path to your .bs file

def parse_bs_file(file_path):
    
    sections = {} # dict with all sessions
    current_section = None

    with open(file_path, 'r') as file:
        for idx,line in enumerate(file,start=1):

            stripped_line = line.rstrip() # remove new line and spaces

            # skip empty lines and comments
            if not stripped_line or stripped_line.startswith('!'): 
                continue

            # checking reserved 
            if stripped_line.startswith('***'):
                
                # with dict
                section_name = stripped_line
                current_section = section_name + ' | ' + str(idx)
                sections[current_section] = []
            
            elif current_section:
                # Append the line to the current section's content
                sections[current_section].append(stripped_line)

    return sections


# print dict
parsed_sections = parse_bs_file(file_path)
print('\n')
for section_name, content in parsed_sections.items():
    print(f"PARSED SECTION NAME: {section_name}")
    # print("\n".join(content))
    print("-" * 100)
