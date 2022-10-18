# importando frameworks
import pandas as pd
import numpy as np
import streamlit as st

# streamlit run app_uber.py

# visualizando os dados
DATA_COLUMN="date/time"
DATA_URL = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"


@st.cache
def load_data(nrows):
    data = pd.read_csv('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz', nrows= nrows)
    # trabalhando o nome das colunas
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    # transformando as datas para datetime
    data["date/time"] = pd.to_datetime(data["date/time"])
    return data

data_load_state = st.text('Carregando dados ...')
data = load_data(10000)
data_load_state.text('Pronto! Carregado.')

if st.checkbox('''Mostrar Raw Data'''):
    st.subheader('Raw Data')
    st.write(data)

st.subheader('Número de Corridas por hora')
# criando histograma
hist_values = np.histogram(data["date/time"].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# interatividade
hour_to_filter = st.slider('Hour', 0,23,17)
filtered_data = data[data[DATA_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa para a hora{}:'.format(hour_to_filter))
st.map(filtered_data)

