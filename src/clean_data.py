import pandas as pd
import os

def clean_energy_data():
    print("Iniciando limpeza e processamento dos dados...")
    
    input_path = 'data/raw/energia_bruto.csv'
    if not os.path.exists(input_path):
        print(f"Erro: Arquivo {input_path} não encontrado. Rode src/generate_data.py primeiro.")
        return
        
    df = pd.read_csv(input_path)
    
    df['Geração_MWh'] = df['Geração_MWh'].fillna(df.groupby('Fonte_Energia')['Geração_MWh'].transform('mean'))
    
    Q1 = df['Custo_Operacional_BRL'].quantile(0.25)
    Q3 = df['Custo_Operacional_BRL'].quantile(0.75)
    IQR = Q3 - Q1
    limite_superior = Q3 + 1.5 * IQR
    
    df.loc[df['Custo_Operacional_BRL'] > limite_superior, 'Custo_Operacional_BRL'] = limite_superior
    
    df['Data'] = pd.to_datetime(df['Data'])
    df['Ano'] = df['Data'].dt.year
    df['Mes'] = df['Data'].dt.month
    df['Custo_por_MWh'] = df['Custo_Operacional_BRL'] / df['Geração_MWh']
    
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/energia_limpo.csv', index=False)
    
    print("Dados limpos com sucesso e salvos em 'data/processed/energia_limpo.csv'")
    print(f"Total de registros finais: {len(df)}")

if __name__ == "__main__":
    clean_energy_data()
