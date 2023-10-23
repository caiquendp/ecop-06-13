import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config('kiq-Ecop06',
    'https://unifei.edu.br/wp-content/themes/twentytwelve-child/img/cabecalho/logo-unifei-oficial.png',
    )

st.title('Pagina alfa Ecop06')

esports = pd.read_csv('https://github.com/MainakRepositor/Datasets/raw/master/GeneralEsportData.csv', enconding='latin-1')

st.dataframe(esports)
