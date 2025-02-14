import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(
    page_title="Temperstura",
    page_icon = "🌡",
    layout= "wide"
)

st.markdown("# Tmperatura 🌡")
st.divider()

if "date" not in st.session_state:
    df_temp = pd.read_excel("dataset/temperatura.xlsx")
    st.session_state["date"] = df_temp
    
df_temp = st.session_state["date"]

codigos = ["Todos"] + list(df_temp["Código"].value_counts().index)
codigo = st.sidebar.selectbox(f"**Código**",codigos)
df_codigos = df_temp[(df_temp['Código'] == codigo)]

if codigo == "Todos":
    df_codigos = df_temp
else:
    df_codigos = df_temp[df_temp["Código"] == codigo]
    
    
st.metric(label="Temperatura", value=df_codigos["Temperatura informada"].iloc[0])

columns = ["Código", "Descrição Matéria Prima", "Fornecedor", "Temperatura informada"]

# Exibição interativa com st.dataframe
st.data_editor(
    df_codigos[columns],
    use_container_width=True,
    column_config={
        "Código": st.column_config.NumberColumn(
            "Código",  # Título da coluna
            format="%.0f",  # Formato arredondado sem casas decimais
        ),
    },
    hide_index=True,  # Esconde o índice
)

    
