# features/space_weather.py
import streamlit as st
from providers.telemetry_provider import fetch_raw_telemetry
from pipelines.telemetry_pipeline import enrich_telemetry_data
from state.session_state import init_session_state

def render_space_weather_tab():
    """
    Renderiza a aba de Clima Espacial e Telemetria.
    """
    st.header("🛰️ Telemetria e Clima Espacial")
    
    # 1. Carregando os dados (Design para Latência)
    with st.spinner("Sincronizando com a rede de satélites lunares..."):
        if st.session_state['telemetry_data'] is None:
            raw_data = fetch_raw_telemetry(num_records=150)
            st.session_state['telemetry_data'] = enrich_telemetry_data(raw_data)
            
    df = st.session_state['telemetry_data']
    
    # 2. Requisito: Filtros Interativos
    st.subheader("Filtros de Missão")
    rover_selecionado = st.selectbox(
        "Selecione a Unidade Rover", 
        options=["Todos"] + list(df['rover_id'].unique())
    )
    
    # Aplicando o filtro
    if rover_selecionado != "Todos":
        df_filtrado = df[df['rover_id'] == rover_selecionado]
    else:
        df_filtrado = df
        
    # 3. Exibição dos dados
    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # 4. Requisito: Feedback Humano (Human-in-the-loop)
    st.subheader("Centro de Comando e Alertas")
    
    # Verifica se há rovers em estado CRÍTICO (🔴)
    rovers_criticos = df_filtrado[df_filtrado['status_risco'] == "🔴"]
    
    if not rovers_criticos.empty:
        st.warning("ALERTA: Rovers em condição crítica detectados na superfície!", icon="⚠️")
        
        # Pega o primeiro rover crítico da lista para a sugestão do sistema
        rover_em_perigo = rovers_criticos.iloc[0]['rover_id']
        
        st.write(f"O sistema de IA sugere o envio imediato de um Drone de Resgate para a unidade **{rover_em_perigo}** devido às condições extremas.")
        
        # Botões de decisão
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Aprovar Envio de Drone 🚁", type="primary"):
                st.session_state['drone_dispatched'] = True
                # Trocamos o st.success por st.toast
                st.toast(f"Drone de resgate despachado para {rover_em_perigo}!", icon="🚁")
        with col2:
            if st.button("Ignorar Alerta", type="secondary"):
                # Trocamos o st.info por st.toast
                st.toast("Alerta ignorado pelo operador.", icon="⚠️")
                
    else:
        st.success("Todos os sistemas operando dentro da normalidade.", icon="✅")