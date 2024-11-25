import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Daten für den Energiequellen-Mix
data = {
  "Jahr": [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 ],
  "Erneuerbare Energie": [63.538, 72.795, 89.999, 95.106, 96.974, 106.446, 125.647, 145.09, 153.677, 163.741, 190.073, 191.106, 217.674, 225.291, 243.589, 253.539, 237.052, 255.366, 273.231 ],
  "Fossile Energie & Kernenergie": [554.8, 550.1, 534.9, 526.4, 487.5, 512.5, 484.8, 465.0, 453.5, 430.8, 410.6, 409.5, 384.2, 369.3, 334.0, 304.3, 334.5, 295.9, 247.5 ]
}

data_eeg = {
    "Jahr": [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Wasserkraft": [19344, 19718, 20811, 20134, 18743, 20682, 17326, 21332, 22660, 19310, 18665, 20215, 19985, 17926, 19957, 18546, 19483, 17458, 19721 ],
    "Windenergie an Land": [27229, 30710, 39713, 40574, 38610, 37619, 48314, 49949, 50803, 55908, 70922, 66324, 86293, 88710, 99166, 102741, 88034, 97738, 114364 ],
    "Windenergie auf See": [0, 0, 0, 0, 38, 174, 568, 722, 905, 1449, 8162, 12092, 17414, 19179, 24379, 26903, 24014, 24752, 23534 ],
    "Photovoltaik": [1282, 2220, 3075, 4420, 6583, 11729, 19599, 26220, 30020, 34753, 37330, 36820, 38001, 43461, 44325, 48525, 49619, 59826, 62330 ],
    "biogene Festbrennstoffe": [6721, 7913, 7824, 8285, 8733, 9247, 9395, 9509, 9392, 9657, 9855, 9673, 9542, 9807, 9790, 10002, 9594, 9525, 8951 ],
    "biogene flüssige Brennstoffe": [117, 726, 958, 1099, 1649, 1291, 386, 319, 286, 333, 425, 481, 428, 381, 330, 308, 201, 89, 102 ],
    "Biogas": [1749, 3450, 8647, 11298, 13599, 15777, 19338, 25143, 26644, 27756, 29184, 29804, 30156, 29358, 29206, 29754, 29639, 29558, 27538 ],
    "Biomethan": [0, 0, 20, 44, 79, 376, 582, 1091, 1672, 2452, 3071, 3070, 2895, 2930, 2923, 2977, 3195, 3024, 3045 ],
    "Klärgas ": [1057, 1023, 999, 1033, 1042, 1093, 1179, 1217, 1215, 1283, 1308, 1331, 1357, 1551, 1578, 1576, 1572, 1544, 1526 ],
    "Deponiegas": [1040, 1046, 962, 826, 713, 600, 595, 512, 461, 416, 384, 343, 324, 279, 262, 233, 215, 188, 175 ],
    "biogener Anteil des Abfalls": [2422, 2965, 3519, 3667, 3352, 3755, 3795, 3971, 4305, 4838, 4565, 4746, 4802, 4932, 4626, 4638, 4575, 4436, 4525 ],
    "Geothermie ": [0, 0, 0, 12, 13, 20, 19, 25, 69, 67, 91, 164, 157, 126, 144, 173, 174, 152, 139 ]
}

df = pd.DataFrame(data)
df_eeg = pd.DataFrame(data_eeg)

#------------------------------------------------
# Streamlit App
st.set_page_config(layout="centered", page_title="Bruttostromerzeugung: Entwicklung der Erneuerbaren Energien", page_icon=":material/wind_power:")


with st.sidebar.expander(label=":material/info: Quellen"):
    st.link_button(label="Bundesministerium für Wirtschaft & Klimaschutz",url="https://www.bmwk.de/Redaktion/DE/Downloads/Energie/erneuerbare-energien-in-de-tischvorlage.pdf?__blob=publicationFile&v=12")
    st.link_button(label="Umweltbundesamt",url="https://www.umweltbundesamt.de/themen/klima-energie/erneuerbare-energien/erneuerbare-energien-in-zahlen#emissionsbilanz")

tab1, tab2 = st.tabs(["Bruttostromerzeugung","Technologien zur Stromerzeugung"])

with tab1:
    # Streamlit App
    st.title(':material/wind_power: Anteile erneuerbarer Energien an der Bruttostromerzeugung in Deutschland')

    # Auswahl des Jahres
    selected_year = st.selectbox('Wähle ein Jahr aus:', df['Jahr'].unique())

    # DataFrame für das ausgewählte Jahr filtern
    filtered_df = df[df['Jahr'] == selected_year].drop(columns='Jahr').T.reset_index()
    filtered_df.columns = ['Art der Energieerzeugung', 'Wert in TWh']

    # Altair Chart erstellen
    chart = alt.Chart(filtered_df).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Wert in TWh", type="quantitative", stack=True),
        color=alt.Color(field="Art der Energieerzeugung", type="nominal"),
        tooltip = ['Art der Energieerzeugung', 'Wert in TWh']
    ).properties(
        title=f'Bruttostromerzeugung im Jahr {selected_year}'
    ).interactive()

    # Diagramm in Streamlit anzeigen
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

with tab2:
    st.title(":material/solar_power: Anteile verschiedener Technologien an der Stromerzeugung durch Erneuerbare Energien")
    
    #Jahresauswahl
    selected_year = st.selectbox('Ein Jahr auswählen:', df_eeg['Jahr'].unique())

    # DataFrame für das ausgewählte Jahr filtern
    filtered_df_eeg = df_eeg[df_eeg['Jahr'] == selected_year].drop(columns='Jahr').T.reset_index()
    filtered_df_eeg.columns = ['Art der Energieerzeugung', 'Wert in GWh']

    # Altair Chart erstellen
    chart = alt.Chart(filtered_df_eeg).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Wert in GWh", type="quantitative", stack=True),
        color=alt.Color(field="Art der Energieerzeugung", type="nominal"),
        tooltip = ['Art der Energieerzeugung', 'Wert in GWh']
    ).properties(
        title=f'Anteile der Technologien im Jahr {selected_year}'
    ).interactive()

    # Diagramm in Streamlit anzeigen
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
    
st.markdown("Stand 25.11.2024")

st.header("**Was bedeutet das?**")
st.markdown("Erneuerbare Energien gewinnen zunehmend an Bedeutung. Im Jahr 2023 wurde erstmals mehr Strom mit Erneuerbaren Energien als mit fossilen Energieträgern & Kernenergie erzeugt. Die Zwischenziele des EEG von 2014 wurden somit diesbezüglich erreicht. Jedoch muss der Ausbau und die Nutzung der Erneuerbaren Energien durch Sektorenkopplung auch außerhalb der Stromerzeugung eine noch größere Rolle spielen.")