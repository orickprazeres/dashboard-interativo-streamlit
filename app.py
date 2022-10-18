# Criando Ambiente Virtual 
# python3 -m venv env

# Abrindo Ambiente Virtual
# ./env/Scripts/Activate.ps1

# importando frameworks
import pandas as pd
import streamlit as st

df = pd.read_csv('criminalidade_sp.csv')

# Rodando o Dashboard
# streamlit run app.py
st.title("Criminalidade em São Paulo")
st.markdown("""
    A **criminalidade** é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de 
    Ciências de Dados conseguimos entender melhor o que está acontecendo e 
    gerar insights que direcionem açõeµes capazes de diminuir os 
    Índices de criminalidade.
""")

st.info("Foram carregadas {} linhas".format(df.shape[0]))

if st.sidebar.checkbox("Mostrar tabela?"):
    st.header("Raw Data")
    st.write(df)

