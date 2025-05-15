import streamlit as st

# Custom CSS para estilizar a página
st.markdown(
    """
    <style>
        /* Fundo branco da página */
        body {
            background-color: white;
        }
        /* Centralizar e estilizar conteúdo principal */
        .main {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2rem;
            border-radius: 10px;
        }
        /* Estilizar título */
        h1 {
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
        }
        /* Centralizar botão */
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Clique no botão abaixo")

# Botão centralizado que mostra a imagem quando clicado
if st.button("Mostrar Stitch"):
    # Usar barra normal no caminho da imagem para funcionar no Streamlit Cloud
    st.image("Imagens/Stitch-2.png", use_container_width=True, caption="💙 Stitch apareceu!")
