import streamlit as st
import pandas as pd

dados = pd.read_csv('estoque.csv')

st.title('Análise de estoque\n')
st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, de uma base de dados de produtos de supermercado')
# Filtro da tabela
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostrar_tabela:
    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options=categorias)

    # Aplicando o filtro
    if categoria != 'Todas':
        df_categoria = dados[dados['Categoria'] == categoria]
    else:
        df_categoria = dados

    # Exibindo a tabela
    st.dataframe(df_categoria)

    # Mostrando a quantidade de linhas
    st.write(f'Número de linhas: {len(df_categoria)}') 

# Função para mostrar a quantidade de linhas (opcional)
def mostra_qntd_linhas(df):
    st.write(f'Número de linhas: {len(df)}')
