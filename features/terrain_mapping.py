import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from providers.terrain_provider import fetch_terrain_data
from pipelines.terrain_pipeline import analyze_landing_zones

def render_terrain_tab():
    # Decorador de cache para otimização de performance (Requisito)
    @st.cache_data
    def load_and_process_terrain():
        raw_data = fetch_terrain_data()
        return analyze_landing_zones(raw_data)

    df = load_and_process_terrain()
    
    # Requisito: Filtros Interativos
    st.subheader("Filtros de Exploração")
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        setor_selecionado = st.selectbox(
            "Selecione o Setor Lunar:", 
            options=["Todos"] + list(df['setor'].unique())
        )
        
    with col_f2:
        inclinacao_maxima = st.slider(
            "Inclinação Máxima Tolerada (Graus):", 
            min_value=0, max_value=45, value=45
        )

    # Aplicação dos filtros
    df_filtrado = df[df['inclinacao_graus'] <= inclinacao_maxima]
    if setor_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['setor'] == setor_selecionado]

    st.divider()

    # Requisito: Visualizações Gráficas
    st.subheader("Análise Topográfica")
    
    # Uso de abas (tabs) para organizar os gráficos (Requisito de UX)
    tab_mapa, tab_estatisticas = st.tabs(["🗺️ Mapa Interativo", "📊 Estatísticas"])
    
    with tab_mapa:
        st.markdown("**Dispersão de Zonas Analisadas (Plotly)**")
        # Gráfico interativo com Plotly (Obrigatório)
        fig_map = px.scatter(
            df_filtrado, 
            x="lon", y="lat", 
            color="status_pouso",
            color_discrete_map={
                "Alto Risco 🔴": "#ff4b4b", 
                "Risco Moderado 🟡": "#ffa421", 
                "Pouso Seguro 🟢": "#21c354"
            },
            hover_data=["inclinacao_graus", "densidade_crateras"],
            title=f"Coordenadas de Pouso - {setor_selecionado}",
            labels={"lon": "Longitude", "lat": "Latitude"}
        )
        st.plotly_chart(fig_map, use_container_width=True)

    with tab_estatisticas:
        st.markdown("**Densidade Média de Crateras por Status (Matplotlib)**")
        if not df_filtrado.empty:
            # Gráfico complementar com Matplotlib
            fig_bar, ax = plt.subplots(figsize=(8, 4))
            medias = df_filtrado.groupby('status_pouso')['densidade_crateras'].mean()
            
            # Mapeamento de cores manual para o matplotlib
            cores = ['#ff4b4b' if 'Alto Risco' in x else '#ffa421' if 'Moderado' in x else '#21c354' for x in medias.index]
            
            medias.plot(kind='bar', ax=ax, color=cores)
            ax.set_ylabel("Densidade Média (%)")
            ax.set_xlabel("Viabilidade")
            plt.xticks(rotation=0)
            
            st.pyplot(fig_bar)
        else:
            st.warning("Nenhum dado encontrado para os filtros atuais.")