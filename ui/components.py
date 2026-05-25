# ui/components.py
import streamlit as st

def render_risk_legend():
    """
    Renderiza a legenda explicativa das cores semânticas na tela.
    """
    st.markdown("""
    **Legenda de Status (Telemetria):**
    * 🔴 **Crítico:** Radiação > 4.0 Sv | Temp > 100°C | Bateria < 20%
    * 🟡 **Alerta:** Radiação > 2.5 Sv | Temp > 60°C
    * 🟢 **Normal:** Condições seguras para operação
    """)