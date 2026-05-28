import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Dashboard Setor Energético", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Análise do Setor Energético Brasileiro")
st.markdown("Dashboard interativo com +50.000 registros de geração de energia, custos operacionais e status de usinas.")

@st.cache_data
def load_data():
    file_path = 'data/processed/energia_limpo.csv'
    if not os.path.exists(file_path):
        st.error("Dados não encontrados. Certifique-se de rodar 'generate_data.py' e 'clean_data.py' primeiro.")
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    df['Data'] = pd.to_datetime(df['Data'])
    return df

df = load_data()

if not df.empty:
    st.sidebar.header("Filtros")
    anos_disponiveis = sorted(df['Ano'].unique())
    ano_selecionado = st.sidebar.multiselect("Selecione o Ano", anos_disponiveis, default=anos_disponiveis)
    
    regioes = df['Região'].unique()
    regiao_selecionada = st.sidebar.multiselect("Selecione a Região", regioes, default=regioes)
    
    fontes = df['Fonte_Energia'].unique()
    fonte_selecionada = st.sidebar.multiselect("Fonte de Energia", fontes, default=fontes)
    
    df_filtrado = df[
        (df['Ano'].isin(ano_selecionado)) & 
        (df['Região'].isin(regiao_selecionada)) &
        (df['Fonte_Energia'].isin(fonte_selecionada))
    ]
    
    st.markdown("### Indicadores Principais")
    col1, col2, col3, col4 = st.columns(4)
    
    total_geracao = df_filtrado['Geração_MWh'].sum() / 1e6
    total_custo = df_filtrado['Custo_Operacional_BRL'].sum() / 1e6
    custo_medio_mwh = df_filtrado['Custo_por_MWh'].mean()
    total_registros = len(df_filtrado)
    
    col1.metric("Total Geração (Mi MWh)", f"{total_geracao:.2f}")
    col2.metric("Custo Total (Mi R$)", f"R$ {total_custo:.2f}")
    col3.metric("Custo Médio por MWh", f"R$ {custo_medio_mwh:.2f}")
    col4.metric("Registros Analisados", f"{total_registros:,.0f}")
    
    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Geração de Energia por Fonte")
        geracao_fonte = df_filtrado.groupby('Fonte_Energia')['Geração_MWh'].sum().reset_index()
        fig_fonte = px.pie(geracao_fonte, values='Geração_MWh', names='Fonte_Energia', hole=0.4,
                           color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_fonte, use_container_width=True)
        
    with col_chart2:
        st.markdown("#### Custo Operacional por Região")
        custo_regiao = df_filtrado.groupby('Região')['Custo_Operacional_BRL'].sum().reset_index()
        fig_regiao = px.bar(custo_regiao, x='Região', y='Custo_Operacional_BRL', 
                            color='Região', text_auto='.2s')
        fig_regiao.update_layout(showlegend=False)
        st.plotly_chart(fig_regiao, use_container_width=True)
        
    st.markdown("#### Evolução Temporal da Geração (Mensal)")
    df_temporal = df_filtrado.groupby(df_filtrado['Data'].dt.to_period('M'))['Geração_MWh'].sum().reset_index()
    df_temporal['Data'] = df_temporal['Data'].dt.to_timestamp()
    fig_temporal = px.line(df_temporal, x='Data', y='Geração_MWh', markers=True)
    fig_temporal.update_layout(xaxis_title="Período", yaxis_title="Geração Total (MWh)")
    st.plotly_chart(fig_temporal, use_container_width=True)
    
    st.markdown("#### Distribuição do Status de Operação")
    status_count = df_filtrado['Status_Operacao'].value_counts().reset_index()
    status_count.columns = ['Status', 'Quantidade']
    fig_status = px.bar(status_count, x='Status', y='Quantidade', color='Status',
                        color_discrete_map={'Normal': '#28a745', 'Manutenção': '#ffc107', 'Falha': '#dc3545'})
    st.plotly_chart(fig_status, use_container_width=True)
