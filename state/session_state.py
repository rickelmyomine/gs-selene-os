import streamlit as st

def init_session_state():
    """
    Inicializa as variáveis globais da aplicação.
    Garante que os dados não sejam perdidos durante o rerun do Streamlit.
    """
    # Armazena os dados processados para não ter que recalcular toda hora
    if 'telemetry_data' not in st.session_state:
        st.session_state['telemetry_data'] = None
        
   # Variável para controle do Drone de Resgate (Feedback Humano)
    if 'drone_dispatched' not in st.session_state:
        st.session_state['drone_dispatched'] = False