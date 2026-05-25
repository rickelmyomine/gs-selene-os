import streamlit as st
from providers.logistics_provider import fetch_resource_data
from pipelines.logistics_pipeline import calculate_extraction_viability

def render_logistics_tab():
    st.subheader("🧊 Prospecção de Recursos Hídricos (Gelo)")

    # Carregando e processando dados
    df_raw = fetch_resource_data()
    df = calculate_extraction_viability(df_raw)

    # Requisito UX/UI: Uso de colunas e métricas de destaque
# Requisito UX/UI: Uso de colunas e métricas de destaque com Deltas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Crateras Mapeadas", len(df), delta="+2 na última órbita")
    with col2:
        total_gelo = df['volume_gelo_estimado_ton'].sum()
        st.metric("Volume Total (Ton)", f"{total_gelo:,.1f}", delta="-15.4 Ton (Sublimação)", delta_color="inverse")
    with col3:
        prioritarios = len(df[df['status_viabilidade'] == 'Prioritário 🟢'])
        st.metric("Alvos Prioritários", prioritarios, delta="1 novo alvo crítico")

    st.divider()

    st.markdown("**Relatório de Viabilidade de Extração**")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()

    # Requisito: Feedback Humano
    st.subheader("Centro de Despacho Logístico")
    
    cratera_alvo = st.selectbox(
        "Selecione a Cratera para enviar Módulo de Extração:", 
        options=df['cratera_alvo']
    )
    
    if st.button("🚀 Autorizar Missão de Extração", type="primary"):
        st.toast(f"Logística aprovada! Equipamentos a caminho de {cratera_alvo}.", icon="🚀")