import streamlit as st

import Notizen

# Logo/Name setzen für Tab in Google, so dass nicht "local" steht
st.set_page_config(
    page_title="Chemieprotokoll"
)

# Seitenleiste-Kommentar erstellen
st.sidebar.success("Wähle einen Tab.")

# Kolone erstellen, um den Titel links zu setzen und nicht in der Mitte
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :green[_Deine lieblings App für Chemieprotokolle!_] :test_tube:')

# Untertitel 
st.subheader('Das Chemieprotokoll unterstützt dich während deinen Labortpraktika bzw. Experimenten während deines Studiums. Hier kannst du deine Experimente dokumentieren, Notizen erstellen oder Berechnungen durchführen.')

#Bild in der 3. Kolone setzen
col3.image('https://pixy.org/src/94/946218.gif')

# Caption erstellen 
st.caption("Erstellt von der BMLD Studentin: Michèle Pfister")


import streamlit as st

options = ['Details', 'Experiment 1', 'Experiment 2', "Experiment 3", "Notizen", "Periodensystem", "Rechner"]
selected_option = st.selectbox('Wählen Sie eine Option aus:', options)

st.write('Sie haben die Option ausgewählt:', selected_option)
