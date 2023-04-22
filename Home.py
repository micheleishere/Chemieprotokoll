import streamlit as st

import Notizen

# Logo/Name setzen für Tab in Google, so dass nicht "local" steht
st.set_page_config(
    page_title="Chemieprotokoll"
)

# Seitenleiste-Kommentar erstellen
import streamlit as st


# Seitenleiste-Kommentar erstellen
st.sidebar.success("Wähle einen Tab.")

import streamlit as st

# Erstelle die Seitenleiste
options = ["Registerkarte 1", "Registerkarte 2", "Registerkarte 3"]
selection = st.sidebar.radio("Gehe zu", options)

# Zeige den Inhalt der ausgewählten Registerkarte an
if selection == "Registerkarte 1":
    st.write("Dies ist der Inhalt von Registerkarte 1")
elif selection == "Registerkarte 2":
    st.write("Dies ist der Inhalt von Registerkarte 2")
else:
    st.write("Dies ist der Inhalt von Registerkarte 3")

# Kolone erstellen, um den Titel links zu setzen und nicht in der Mitte
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :green[_Deine lieblings App für Chemieprotokolle!_] :test_tube:')

# Untertitel 
st.subheader('Das Chemieprotokoll unterstützt dich während deinen Labortpraktika bzw. Experimenten während deines Studiums. Hier kannst du deine Experimente dokumentieren, Notizen erstellen oder Berechnungen durchführen.')

#Bild in der 3. Kolone setzen
col3.image('https://synaigy-wbg-media-s3.s3.eu-central-1.amazonaws.com/media/image/6f/8f/42/Chemie-Kachel5cd3c9c0aaeff.jpg')

# Caption erstellen 
st.caption("Erstellt von der BMLD Studentin: Michèle Pfister")


import streamlit as st

options = ['Details', 'Experiment 1', 'Experiment 2', "Experiment 3", "Notizen", "Periodensystem", "Rechner"]
selected_option = st.selectbox('Wählen Sie eine Option aus:', options)

st.write('Sie haben die Option ausgewählt:', selected_option)

import streamlit as st

notiz = st.text_area('Geben Sie Ihre Notiz ein:', '', height=100, max_chars=1000)
st.write('Ihre Notiz:', notiz)

import streamlit as st
import datetime 

# Kolone erstellen, dass Titel links und Emoji rechts
col1, col2, col3 = st.columns([1,2,1])
st.markdown(' # :green[_Versuch 1_]')
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
