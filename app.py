import streamlit as st
import pandas as pd

dados = pd.read_csv('estoque.csv')

st.title('Análise de estoque\n')
st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, de uma base de dados de produtos de supermercado')
