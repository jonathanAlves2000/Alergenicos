import streamlit as st
import pandas as pd
import openpyxl
from PIL import Image

st.set_page_config(
    page_title = "Alergênicos",
    page_icon = "imagens\etiqueta-de-preco.png",
    layout= "wide"
)

st.markdown("# Materiais Alergênicos ❗")


if "data" not in st.session_state:
    df_data = pd.read_excel("dataset\\alergenicos.xlsx")
    st.session_state["data"] = df_data
    
df_data = st.session_state["data"]

alergeno_imagens ={
    "CEREAIS COM GLÚTEN": "imagens\Glútem.png",
    "LEITE E DERIVADOS": "imagens\Leite.png",
    "SULFITO": "imagens\Sulfito.png",
    "SOJA E DERIVADOS": "imagens\Soja.png",
    "PEIXE E DERIVADOS": "imagens\Peixe.png"
}

code = df_data["CÓDIGO"].value_counts().index
cod = st.sidebar.selectbox("Código", code)
df_code = df_data[(df_data["CÓDIGO"] == cod)]

if not df_code.empty:
    # Mostrar informações do código selecionado
    st.dataframe(df_code)

    # Criar lista de imagens para exib
    imagens_para_exibir = []
    legendas = []
    for coluna, imagem_caminho in alergeno_imagens.items():
        if df_code.iloc[0][coluna] == "X":  # Verifica se o alérgeno está presente
            imagens_para_exibir.append(imagem_caminho)
            legendas.append(coluna)

    # Exibir imagens lado a lado
    if imagens_para_exibir: 
        cols = st.columns(len(imagens_para_exibir))  # Cria uma coluna para cada imagem
        for col, imagem_caminho, legenda in zip(cols, imagens_para_exibir, legendas):
            with col:
                imagem = Image.open(imagem_caminho)
                st.image(imagem, caption=legenda, width=450)
    else:
        st.info("Nenhum alérgeno identificado para este código, Porém não armazenar próximo de MP ou HALB com Alergênicos.")
else:
    st.error("Nenhum dado encontrado para o código selecionado.")

st.sidebar.markdown("Desenvolvido por [Jonathan Alves](https://www.linkedin.com/in/jonathan-alves-408283183/)")



