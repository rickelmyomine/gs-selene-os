import streamlit as st
from state.session_state import init_session_state
from features.space_weather import render_space_weather_tab
from ui.components import render_risk_legend
from features.terrain_mapping import render_terrain_tab
from features.logistics import render_logistics_tab

# 1. Configuração da página (deve ser a primeira função chamada)
st.set_page_config(
    page_title="SeleneOS - Lunar Dashboard",
    page_icon="🌑",
    layout="wide"
)

# 2. Inicializa o estado global da aplicação
init_session_state()

# 3. Construção da Sidebar (Barra Lateral)
with st.sidebar:
    # --- ADICIONADO AGORA: Logotipo do sistema ---
    try:
        st.image("assets/logo.png", use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Logotipo não encontrado. Coloque um 'logo.png' na pasta 'assets'.")
    # ---------------------------------------------
    
    st.title("🌑 SeleneOS")
    st.markdown("Painel de Controlo Lunar")
    st.divider()
    
    # Menu de navegação
    opcao_menu = st.radio(
        "Módulos Operacionais:",
        ["🛰️ Clima Espacial", "🗺️ Terreno", "📦 Logística"]
    )
    
    st.divider()
    st.caption("Sistema de Suporte a Decisão - v1.0")
# 4. Renderização Dinâmica (Baseada na escolha da Sidebar)
if opcao_menu == "🛰️ Clima Espacial":
    st.title("🛰️ Monitorização de Clima Espacial")
    st.markdown("Sistema integrado de telemetria e controlo de radiação.")
    st.divider()
    
    # Chama o componente da funcionalidade
    render_space_weather_tab()
    
    st.divider()
    # Exibe a legenda na parte inferior
    render_risk_legend()

elif opcao_menu == "🗺️ Terreno":
    st.title("🗺️ Mapeamento de Terreno")
    st.markdown("Análise topográfica para pouso de módulos lunares.")
    st.divider()
    
    render_terrain_tab()

elif opcao_menu == "📦 Logística":
    st.title("📦 Controlo Logístico de Extração")
    st.markdown("Gestão de recursos hídricos e despacho de equipamentos.")
    st.divider()
    
    render_logistics_tab()