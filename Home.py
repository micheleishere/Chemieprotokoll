import streamlit as st

import Notizen

# Logo/Name setzen für Tab in Google, so dass nicht "local" steht
st.set_page_config(
    page_title="Chemieprotokoll"
)

# Seitenleiste-Kommentar erstellen
import streamlit as st

st.sidebar.header('Optionen')

import streamlit as st

# Sidebar-Tabs erstellen
tabs = st.sidebar.multiselect(
    'Wählen Sie eine Registerkarte',
    ['Tab 1', 'Tab 2', 'Tab 3']
)

# Inhalte für jede Registerkarte definieren
if 'Tab 1' in tabs:
    st.sidebar.write('Details')

if 'Tab 2' in tabs:
    st.sidebar.write('Experiment 1')

if 'Tab 3' in tabs:
    st.sidebar.write('Experiment 2')

st.write('Sie haben die Option ausgewählt:', auswahl)

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

notiz = st.text_area('Geben Sie Ihre Notiz ein:', '', height=100, max_chars=500)
st.write('Ihre Notiz:', notiz)
