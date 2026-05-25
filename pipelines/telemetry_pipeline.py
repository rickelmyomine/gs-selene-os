import pandas as pd

def enrich_telemetry_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e classifica os dados brutos de telemetria para a interface.
    """
    df_clean = df.copy()
    
    # Arredondando valores para melhor visualização na UI
    df_clean['radiation_sv'] = df_clean['radiation_sv'].round(2)
    df_clean['temperature_c'] = df_clean['temperature_c'].round(1)
    df_clean['battery_pct'] = df_clean['battery_pct'].round(0)
    
    # Classificação de Risco (Regras de Negócio) com Emojis
    def classify_risk(row):
        if row['radiation_sv'] > 4.0 or row['temperature_c'] > 100 or row['battery_pct'] < 20:
            return "🔴" # Crítico
        elif row['radiation_sv'] > 2.5 or row['temperature_c'] > 60:
            return "🟡" # Alerta
        else:
            return "🟢" # Normal
            
    df_clean['status_risco'] = df_clean.apply(classify_risk, axis=1)
    
    # Ordenando pelos eventos mais recentes
    df_clean = df_clean.sort_values(by="timestamp", ascending=False)
    
    return df_clean