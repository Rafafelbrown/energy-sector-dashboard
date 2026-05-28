import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_energy_data(num_records=55000):
    print(f"Gerando {num_records} registros de dados de energia...")
    
    np.random.seed(42)
    
    regions = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    sources = ['Hidrelétrica', 'Eólica', 'Solar', 'Termelétrica', 'Nuclear']
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    
    random_days = np.random.randint(0, 5*365, num_records)
    dates = [start_date + timedelta(days=int(d)) for d in random_days]
    
    data = {
        'Data': dates,
        'Região': np.random.choice(regions, num_records, p=[0.1, 0.25, 0.15, 0.35, 0.15]),
        'Fonte_Energia': np.random.choice(sources, num_records, p=[0.5, 0.2, 0.1, 0.15, 0.05]),
        'Geração_MWh': np.random.normal(loc=500, scale=150, size=num_records).round(2),
        'Custo_Operacional_BRL': np.random.normal(loc=15000, scale=5000, size=num_records).round(2),
        'Status_Operacao': np.random.choice(['Normal', 'Manutenção', 'Falha'], num_records, p=[0.85, 0.10, 0.05])
    }
    
    df = pd.DataFrame(data)
    
    null_indices = np.random.choice(df.index, size=int(num_records * 0.02), replace=False)
    df.loc[null_indices, 'Geração_MWh'] = np.nan
    
    anomaly_indices = np.random.choice(df.index, size=int(num_records * 0.01), replace=False)
    df.loc[anomaly_indices, 'Custo_Operacional_BRL'] = df.loc[anomaly_indices, 'Custo_Operacional_BRL'] * 10
    
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/energia_bruto.csv', index=False)
    print("Dados brutos gerados com sucesso em 'data/raw/energia_bruto.csv'")

if __name__ == "__main__":
    generate_energy_data()
