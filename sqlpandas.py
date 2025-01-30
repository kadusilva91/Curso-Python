import mysql.connector
import pandas as pd

#conectar ao servidor MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cadastro"
)

#Ler a tabela desejada para um DataFrame em pandas
df = pd.read_sql("SELECT * FROM gafanhotos",conexao)

#fechar a conexão com o servidor MySQL
conexao.close()

#Agora você pode manipular o DataFrame como quiser
print(df.head())