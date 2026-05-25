import pandas as pd

def analyze_landing_zones(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a viabilidade de aterragem baseada na inclinação e nas crateras.
    """
    df_clean = df.copy()
    
    # Regras de Negócio: Cálculo de Risco de Aterragem
    def calculate_safety(row):
        if row['inclinacao_graus'] > 25 or row['densidade_crateras'] > 75:
            return "Alto Risco 🔴"
        elif row['inclinacao_graus'] > 15 or row['densidade_crateras'] > 40:
            return "Risco Moderado 🟡"
        else:
            return "Pouso Seguro 🟢"
            
    df_clean['status_pouso'] = df_clean.apply(calculate_safety, axis=1)
    
    # Arredondamentos para UI
    df_clean['inclinacao_graus'] = df_clean['inclinacao_graus'].round(1)
    df_clean['densidade_crateras'] = df_clean['densidade_crateras'].round(1)
    df_clean['lat'] = df_clean['lat'].round(4)
    df_clean['lon'] = df_clean['lon'].round(4)
    
    return df_clean