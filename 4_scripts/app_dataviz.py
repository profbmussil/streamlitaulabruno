import streamlit as st
import pandas as pd
import plotly.express as px


st.title('**Futebol APP**')
# titulo aplicação
st.write('Site de estatísticas esportivas')

st.sidebar.header('Escolha os times')

df = pd.read_csv('../1_bases_tratadas/dadostratados.csv', sep=';', encoding='utf-8')

times = df['home_team_name'].drop_duplicates()
escolha_time = st.sidebar.selectbox("Escolha um time",times)

df2 = df[df['home_team_name']==escolha_time]

fig = px.box(df2, x='home_ppg')
st.plotly_chart(fig)

fig2 = px.histogram(df2.home_ppg)
st.plotly_chart(fig2)

fig3 = px.scatter(df2,'home_ppg','over_25_percentage_pre_match')
st.plotly_chart(fig3)

fig4 = px.pie(df2, 'placar')
st.plotly_chart(fig4)

st.title('Indicadores gerais')
col1, col2, col3 = st.columns(3)
col1.metric("Pontos médios", value=round(df2.home_ppg.mean(),2))
col2.metric("Gols médios", value=round(df2.home_team_goal_count.mean(), 2))
col3.metric("Escanteios médios", value=round(df2.home_team_corner_count.mean(), 2))


col1, col2 = st.columns(2)
df3 = df2.groupby('placar')[['home_team_name']].count().reset_index().rename(columns={'home_team_name':'qtd'})
print(df3)
figpiz = px.pie(data_frame=df3, values='qtd', names='placar')
figcaixa = px.box(df2, x='home_ppg')
col1.plotly_chart(figpiz, use_container_width=True)
col2.plotly_chart(figcaixa, use_container_width=True)