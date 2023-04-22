import streamlit as st
import datetime 

# Kolone erstellen, dass Titel links und Emoji rechts
col1, col2, col3 = st.columns([1,2,1])
st.markdown(' # :blue[_Experiment 1_]')
col3.header(':test_tube:')

# Trennungslinie hinzufügen
st.write("---")

# Eingabe Titel 
title = st.text_input('Titel Experiment', ' ')

# Kalender hinzufügen
d = st.date_input(
    "Datum des Experiments",
    datetime.date(2023, 3, 31))

# Input Eingabe
title = st.text_input('Durchgeführt von', ' ')

title = st.text_input('Studiengang', ' ')

# Multiselektion 
options = st.multiselect(
    'Verwendetes Material',
    ['Erlenmeyerkolben', 'Messzylinder', 'Trichter', 'Polylöffel', 'Becherglas', 'Magnetstab mit Fischli', 'Messkolben', 'Bürette', 'Thermometer', 'Glasstab','Anderes'],
    ['Erlenmeyerkolben', 'Messzylinder'])

# Input Text 
txt = st.text_area('Verwendete Chemikalien: ')
st.write('Output:',txt)

txt = st.text_area('Ablauf des Experiments: ')
st.write('Ablauf Output:',txt)

txt = st.text_area('Schlussfolgerungen: ')
st.write('Schlussfolgerungen Output:',txt)
