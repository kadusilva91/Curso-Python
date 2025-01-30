import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\Kadu\\OneDrive\\Área de Trabalho\\Olympics 2024.csv")
print(df.head())
print(df.info())

# Limpeza dos Dados
df.isnull().sum()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Análise Univariada - distribuição das medalhas
medalhas = df[['Gold', 'Silver', 'Bronze']].sum()
medalhas.plot(kind='bar')
plt.title('Distribuição de Medalhas (Ouro, Prata, Bronze)')
plt.ylabel('Quantidade')
plt.show()

# Países com mais medalhas
df['Total'] = df['Gold'] + df['Silver'] + df['Bronze']
top_paises = df[['NOC', 'Total']].sort_values(by='Total', ascending=False).head(10)
top_paises.plot(x='NOC', y='Total', kind='bar')
plt.title('Top 10 Países Com Mais Medalhas')
plt.ylabel('Total de Medalhas')
plt.show()

# Análise Bivariada e Multivariada - correlação entre medalhas
sns.heatmap(df[['Gold', 'Silver', 'Bronze']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlação Entre Medalhas de Ouro, Prata e Bronze')
plt.show()

# Relação entre Ranking e Medalhas
sns.scatterplot(data=df, x='Rank', y='Total')
plt.title('Relação Entre Ranking e Total de Medalhas')
plt.xlabel('Ranking')
plt.ylabel('Total de Medalhas')
plt.show()