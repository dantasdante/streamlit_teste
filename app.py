import streamlit as st
import joblib
import pandas as pd

modelo = joblib.load("mdl.pkl")

st.title("Modelo de Classificação - Doença Cardíaca")

#  Inputs numéricos
age = st.number_input("Idade", min_value=1, max_value=120, step=1)
restingBP = st.number_input("Pressão Arterial em Repouso", min_value=50, max_value=200, step=1)
cholesterol = st.number_input("Colesterol", min_value=100, max_value=600, step=1)
fastingBS = st.radio("Glicose em Jejum > 120 mg/dl?", ["Não", "Sim"])  # 0 para Não, 1 para Sim
maxHR = st.number_input("Frequência Cardíaca Máxima", min_value=50, max_value=250, step=1)
oldpeak = st.number_input("Oldpeak (Depressão do ST)", min_value=0.0, max_value=10.0, step=0.1)

#  Inputs categóricos (convertidos para variáveis dummy)
sex = st.radio("Sexo", ["Masculino", "Feminino"])
chest_pain_type = st.selectbox("Tipo de Dor no Peito", ["ASY", "ATA", "NAP", "TA"])
resting_ecg = st.selectbox("Eletrocardiograma", ["LVH", "Normal", "ST"])
exercise_angina = st.radio("Angina Induzida por Exercício?", ["Não", "Sim"])
st_slope = st.selectbox("Inclinação do Segmento ST", ["Down", "Flat", "Up"])

# Converter entradas categóricas para 0 e 1 (One-Hot Encoding)
data = {
    "col_0": age,
    "col_1_F": 1 if sex == "Feminino" else 0,
    "col_1_M": 1 if sex == "Masculino" else 0,
    "col_2_ASY": 1 if chest_pain_type == "ASY" else 0,
    "col_2_ATA": 1 if chest_pain_type == "ATA" else 0,
    "col_2_NAP": 1 if chest_pain_type == "NAP" else 0,
    "col_2_TA": 1 if chest_pain_type == "TA" else 0,
    "col_3": restingBP,
    "col_4": cholesterol,
    "col_5": 1 if fastingBS == "Sim" else 0,
    "col_6_LVH": 1 if resting_ecg == "LVH" else 0,
    "col_6_Normal": 1 if resting_ecg == "Normal" else 0,
    "col_6_ST": 1 if resting_ecg == "ST" else 0,
    "col_7": maxHR,
    "col_8_N": 1 if exercise_angina == "Não" else 0,
    "col_8_Y": 1 if exercise_angina == "Sim" else 0,
    "col_9": oldpeak,
    "col_10_Down": 1 if st_slope == "Down" else 0,
    "col_10_Flat": 1 if st_slope == "Flat" else 0,
    "col_10_Up": 1 if st_slope == "Up" else 0
}

# Criar DataFrame com os dados inseridos
entrada = pd.DataFrame([data])

#Botão para fazer a previsão
if st.button("Prever"):
    predicao = modelo.predict(entrada)
    st.write(f"Resultado da Classificação: **{predicao[0]}**")
