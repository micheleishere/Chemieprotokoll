import streamlit as st

import Notizen

# Logo/Name setzen für Tab in Google, so dass nicht "local" steht
st.set_page_config(
    page_title="Laborjournal ZHAW"
)

# Seitenleiste-Kommentar erstellen
st.sidebar.success("Wähle einen Tab.")

# Kolone erstellen, um den Titel links zu setzen und nicht in der Mitte
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :blue[_Welcome to our App Laborjournal ZHAW_] :test_tube:')

# Untertitel 
st.subheader('Die Laborjournal ZHAW App unterstützt dich bei deinen Labortpraktika bzw. Experimenten während deines Studiums. Hier kannst du deine Experimente dokumentieren, Notizen erstellen oder Berechnungen durchführen.')

#Bild in der 3. Kolone setzen
col3.image('https://pixy.org/src/94/946218.gif')

# Caption erstellen 
st.caption('Erstellt von BMLD Studentinnen: Lea Gugganig, Michèle Pfister und Ivana Vujinovic')


options = st.selectbox("wähle seite", ["notizen"])

if options == "notizen":
    Notizen