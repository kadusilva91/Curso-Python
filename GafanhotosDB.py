import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cadastro"
)
cursor = conexao.cursor()

comando = 'SELECT * FROM cursos'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()