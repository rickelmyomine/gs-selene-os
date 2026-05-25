import pandas as pd
import numpy as np

def fetch_resource_data():
    """
    Simula dados de prospecção de gelo em crateras lunares.
    """
    np.random.seed(42)
    craters = ["Shackleton", "Shoemaker", "Faustini", "Cabeus", "Haworth"]
    
    data = {
        "cratera_alvo": craters,
        "volume_gelo_estimado_ton": np.random.uniform(500, 8000, len(craters)),
        "dificuldade_extracao": np.random.choice(["Baixa", "Média", "Alta"], len(craters)),
        "distancia_base_km": np.random.uniform(5, 120, len(craters))
    }
    
    return pd.DataFrame(data)