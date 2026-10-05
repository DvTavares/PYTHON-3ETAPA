import streamlit as st
import pandas as pd

st.write("Olá, mundo")

nome = "Davi"
idade = 18

st.write(nome, idade)

st.title("Meu primeiro dash")
st.subheader("Davi")

df = pd.DataFrame({
    'Matéria': ['Português', 'Matemática', 'Python', 'Frame'],
    'Nota': [5, 9, 7, 10]
})

st.write(df)
