import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def fetch_raw_telemetry(num_records=100):
    """
    Simula a busca de dados brutos de telemetria dos rovers lunares.
    Métricas: Radiação (Sv), Temperatura (°C), Bateria (%).
    """
    np.random.seed(42) # Mantém os dados consistentes para testes
    
    # Gerando timestamps das últimas horas
    now = datetime.now()
    timestamps = [now - timedelta(minutes=i*15) for i in range(num_records)]
    
    # Simulando os sinais dos sensores
    data = {
        "timestamp": timestamps,
        "rover_id": np.random.choice(["Rover-Alpha", "Rover-Beta", "Rover-Gamma"], num_records),
        "radiation_sv": np.random.uniform(0.1, 5.5, num_records), # Radiação em Sieverts
        "temperature_c": np.random.uniform(-150, 120, num_records), # Extremos lunares
        "battery_pct": np.random.uniform(10, 100, num_records)
    }
    
    return pd.DataFrame(data)