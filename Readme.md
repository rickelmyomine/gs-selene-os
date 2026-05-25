🌑 SeleneOS: Lunar Operations Dashboard1. Descrição do ProblemaA exploração lunar contínua exige monitoramento constante para garantir a segurança de equipamentos e o planejamento estratégico de missões. Eventos climáticos espaciais (tempestades solares), as irregularidades do terreno e a complexidade na extração de recursos (gelo/água) geram volumes massivos de dados que precisam ser interpretados rapidamente. O SeleneOS resolve esse problema consolidando essas informações em uma interface única e interativa, permitindo que tomadores de decisão apliquem ações preventivas e logísticas em tempo real, sem a necessidade de conhecimento técnico profundo dos dados brutos.  

2. Fonte de DadosPara o desenvolvimento da Prova de Conceito (POC), os dados utilizados são simulados e estruturados em formato tabular (CSV/JSON), representando:Telemetria Solar: Níveis de radiação e temperatura em tempo real.Topografia: Coordenadas espaciais, inclinação de terreno e densidade de crateras.  Espectrometria: Volumes detectados de recursos hídricos em zonas de sombra permanente.  

3. Justificativa do FrameworkO framework escolhido foi o Streamlit. A escolha se justifica pela eficiência em conectar scripts analíticos em Python diretamente a componentes de interface web reativos. O Streamlit facilita o gerenciamento do ciclo de execução através do st.session_state e otimiza a performance com decoradores de cache (@st.cache_data), o que é fundamental para não onerar o processamento ao recalcular dados topográficos ou aplicar filtros interativos.  

4. Diagrama de ArquiteturaO projeto foge do padrão monolítico e adota uma arquitetura em camadas, organizada nos seguintes diretórios:  /providers: Simulação e consumo de dados brutos (telemetria, clima, geolocalização).  /pipelines: Limpeza, cálculo de risco e enriquecimento dos dados.  /state: Gerenciamento centralizado de variáveis de sessão (ex: modo de segurança ativado).  /ui: Componentes visuais isolados (gráficos, modais, cards).  /features: Telas do sistema (Clima Espacial, Terreno, Logística) agrupando as responsabilidades.  

5. Instruções de Instalação e ExecuçãoPré-requisitos: 
Python 3.9+ instalado.

Clone o repositório

Crie e ative um ambiente virtual:
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Execute a aplicação:
streamlit run app.py