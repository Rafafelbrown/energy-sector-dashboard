# ⚡ Análise do Setor Energético — Dashboard com +50k Registros

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Data_Visualization-3F4F75?logo=plotly)
![Power BI](https://img.shields.io/badge/Power_BI-Ready-F2C811?logo=powerbi)

## 📖 Sobre o Projeto

Este projeto consiste em um pipeline de dados completo focado no setor energético. O objetivo foi coletar (simular), processar, limpar e visualizar um dataset com mais de **50.000 registros** relacionados à geração de energia, fontes (Renováveis, Fósseis, Nucleares), custos operacionais e status das usinas.

Aplica técnicas de **ETL (Extract, Transform, Load)** usando `Pandas` para tratar dados ausentes e anomalias, culminando na criação de um dashboard interativo (Streamlit/Plotly) que fornece insights estratégicos — imitando a robustez e visão de negócios de relatórios criados em **Power BI**.

O dado gerado também pode ser facilmente importado para o Power BI ou Excel para criação de dashboards corporativos.

## 🎯 Principais Funcionalidades

- **Geração de Dados Realistas:** Script em Python capaz de gerar milhares de registros imitando bases de dados do setor de energia.
- **Limpeza e Tratamento:** Uso avançado de Pandas para tratar valores ausentes (imputação pela média da categoria) e Outliers (método do Intervalo Interquartil - IQR).
- **Dashboard Interativo:** Uma aplicação web em Streamlit com gráficos dinâmicos usando Plotly.
- **Métricas de Negócio:** KPIs como "Custo Médio por MWh", "Total de Geração" e "Evolução Temporal".

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem base do projeto.
- **Pandas & NumPy**: Manipulação, limpeza e engenharia de features.
- **Plotly**: Visualização de dados dinâmica e interativa.
- **Streamlit**: Criação rápida do dashboard em Python.
- *(Opcional)* **Power BI / Excel**: O arquivo de saída `energia_limpo.csv` está estruturado para ser conectado como fonte de dados no Power BI.

## 🚀 Como Executar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/Rafafelbrown/energy-sector-dashboard
cd energy-sector-dashboard
```

### 2. Crie e ative um ambiente virtual (Recomendado)
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Pipeline de Dados
Gere os dados brutos (+55.000 registros):
```bash
python src/generate_data.py
```
Execute a limpeza e transformação:
```bash
python src/clean_data.py
```

### 5. Inicie o Dashboard
```bash
streamlit run src/dashboard.py
```

## 📊 Insights Extraídos (Exemplos)

1. **Eficiência de Custos:** Fontes renováveis apresentaram variações menores de custo operacional ao longo dos meses.
2. **Impacto de Falhas:** Usinas em status de "Falha" geraram um custo extra de manutenção, destacando a necessidade de manutenção preventiva.
3. **Distribuição Regional:** A região Sudeste possui a maior parcela de geração, de acordo com o peso probabilístico estipulado.

## 🤝 Contato

Desenvolvido para compor Análise de Dados.
Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/rafael-brown/).
