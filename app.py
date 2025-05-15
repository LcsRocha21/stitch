import streamlit as st

# Deixar fundo branco (streamlit já tem fundo branco padrão)
st.markdown(
    """
     <style>
        body {
            background-color: white;
        }
        .main {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
        }
        h1 {
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
        }
        .stButton {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Clique no botão abaixo")

if st.button("Mostrar Stitch"):
    st.image("Imagens\Stitch-2.png", use_container_width=True)
