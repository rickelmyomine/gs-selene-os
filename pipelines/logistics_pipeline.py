import pandas as pd

def calculate_extraction_viability(df: pd.DataFrame) -> pd.DataFrame:
    """
    Avalia a viabilidade logística para extração de recursos.
    """
    df_clean = df.copy()
    
    # Arredondamentos
    df_clean['volume_gelo_estimado_ton'] = df_clean['volume_gelo_estimado_ton'].round(1)
    df_clean['distancia_base_km'] = df_clean['distancia_base_km'].round(1)

    # Regra de Negócio: Viabilidade Logística
    def score_viability(row):
        if row['dificuldade_extracao'] == 'Alta' or row['distancia_base_km'] > 100:
            return "Inviável 🔴"
        elif row['dificuldade_extracao'] == 'Média':
            return "Requer Análise 🟡"
        else:
            return "Prioritário 🟢"

    df_clean['status_viabilidade'] = df_clean.apply(score_viability, axis=1)
    
    # Ordenar pelas prioridades e maior volume
    df_clean = df_clean.sort_values(by=['status_viabilidade', 'volume_gelo_estimado_ton'], ascending=[False, False])
    
    return df_clean