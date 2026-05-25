import pandas as pd
import numpy as np

def fetch_terrain_data(num_points=300):
    """
    Simula a obtenção de dados topográficos da superfície lunar.
    Métricas: Latitude, Longitude, Inclinação e Densidade de Crateras.
    """
    np.random.seed(42) # Mantém consistência nos dados gerados
    
    data = {
        "setor": np.random.choice(["Polo Sul", "Mar da Tranquilidade", "Cratera Tycho"], num_points),
        "lat": np.random.uniform(-90, 90, num_points),
        "lon": np.random.uniform(-180, 180, num_points),
        "inclinacao_graus": np.random.uniform(0, 45, num_points), # 0 a 45 graus
        "densidade_crateras": np.random.uniform(0, 100, num_points) # 0 a 100%
    }
    
    return pd.DataFrame(data)