import pandas as pd
from sqlalchemy import create_engine

# importar arquivo cvs
dados = pd.read_csv('ecom.csv', sep= ',')

# visualizar as primeiras linhas do dataset
print(dados.head())

# visualizar se há valores nulos 
print(dados.isnull().sum())

# como não há valores nulos, vamos visualizar informações gerais sobre o dataset
print(dados.info())

engine = create_engine('mysql+pymysql://')