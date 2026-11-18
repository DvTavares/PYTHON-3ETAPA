import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel IQVU - Belo Horizonte", layout="wide")

cols = ["NOMEUP", "ANO", "SERIE", "IQVU", "Educacao", "Saude", "Habitacao", "Infraestrutura", "Cultura"]
linhas = [
    ("Taquaril", 1994, "SERIE HISTORICA", 0.412, 0.39, 0.42, 0.45, 0.38, 0.42),
    ("Taquaril", 2000, "SERIE HISTORICA", 0.448, 0.43, 0.45, 0.48, 0.42, 0.46),
    ("Taquaril", 2006, "SERIE HISTORICA", 0.485, 0.47, 0.49, 0.51, 0.46, 0.49),
    ("Taquaril", 2010, "SERIE HISTORICA", 0.512, 0.50, 0.52, 0.54, 0.49, 0.51),
    ("Taquaril", 2012, "SERIE HISTORICA", 0.530, 0.52, 0.54, 0.55, 0.51, 0.53),
    ("Taquaril", 2014, "SERIE HISTORICA", 0.549, 0.54, 0.55, 0.57, 0.53, 0.55),
    ("Taquaril", 2016, "SERIE HISTORICA", 0.568, 0.56, 0.57, 0.59, 0.55, 0.57),
    ("Santa Ines", 1994, "SERIE HISTORICA", 0.615, 0.63, 0.60, 0.64, 0.61, 0.59),
    ("Santa Ines", 2000, "SERIE HISTORICA", 0.642, 0.66, 0.63, 0.66, 0.64, 0.62),
    ("Santa Ines", 2006, "SERIE HISTORICA", 0.678, 0.69, 0.67, 0.70, 0.67, 0.66),
    ("Santa Ines", 2010, "SERIE HISTORICA", 0.705, 0.72, 0.70, 0.72, 0.69, 0.69),
    ("Santa Ines", 2012, "SERIE HISTORICA", 0.721, 0.74, 0.71, 0.74, 0.71, 0.70),
    ("Santa Ines", 2014, "SERIE HISTORICA", 0.739, 0.75, 0.73, 0.76, 0.73, 0.72),
    ("Santa Ines", 2016, "SERIE HISTORICA", 0.756, 0.77, 0.75, 0.78, 0.74, 0.74),
    ("Taquaril", 2016, "NOVA SERIE", 0.510, 0.50, 0.51, 0.52, 0.50, 0.52),
    ("Santa Ines", 2016, "NOVA SERIE", 0.710, 0.72, 0.70, 0.71, 0.70, 0.72),
    ("Centro", 2016, "SERIE HISTORICA", 0.812, 0.80, 0.82, 0.81, 0.83, 0.80),
]
df = pd.DataFrame(linhas, columns=cols)

df_filtrado = df[
    df["NOMEUP"].isin(["Taquaril", "Santa Ines"]) & (df["SERIE"] == "SERIE HISTORICA")
].copy()
df_tabela = df_filtrado[["NOMEUP", "ANO", "IQVU"]]

CORES = {"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"}

dimensoes = {"Educacao": "Educação", "Saude": "Saúde", "Habitacao": "Habitação",
             "Infraestrutura": "Infraestrutura", "Cultura": "Cultura"}
d2016 = df_filtrado[df_filtrado["ANO"] == 2016]
dados_dim = (
    d2016.melt(id_vars="NOMEUP", value_vars=list(dimensoes), var_name="Dimensao", value_name="Valor")
    .rename(columns={"NOMEUP": "Bairro"})
)
dados_dim["Dimensao"] = dados_dim["Dimensao"].map(dimensoes)

dados_empilhado = dados_dim[["Bairro", "Dimensao", "Valor"]]
dados_radar = dados_dim.rename(columns={"Valor": "Nota"})[["Bairro", "Dimensao", "Nota"]]
dados_pizza = d2016[["NOMEUP", "IQVU"]].rename(columns={"NOMEUP": "Bairro"})

st.title("Painel Streamlit do IQVU de Belo Horizonte — Taquaril e Santa Inês")
st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela do IQVU (Série Histórica)")
    st.dataframe(df_tabela, width="stretch", hide_index=True)

else:
    st.header("Gráficos do IQVU — Taquaril e Santa Inês")

    st.subheader("1. Gráfico de Linha — Taquaril")
    fig1 = px.line(df_tabela[df_tabela["NOMEUP"] == "Taquaril"], x="ANO", y="IQVU", markers=True,
                   title="Evolução do IQVU — Taquaril (1994 a 2016)", template="plotly_dark")
    fig1.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig1.update_xaxes(type="category")
    st.plotly_chart(fig1, width="stretch")

    st.subheader("2. Gráfico de Linha — Santa Inês")
    fig2 = px.line(df_tabela[df_tabela["NOMEUP"] == "Santa Ines"], x="ANO", y="IQVU", markers=True,
                   title="Evolução do IQVU — Santa Inês (1994 a 2016)", template="plotly_dark")
    fig2.update_traces(line_color="#00F5D4", line_width=3, marker_size=8)
    fig2.update_xaxes(type="category")
    st.plotly_chart(fig2, width="stretch")

st.markdown("---")
st.caption("Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte — https://dados.pbh.gov.br/")