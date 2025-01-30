#importando o mysql que foi instalado
import mysql.connector

# conectando o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbyoutube"
)

cursor = conexao.cursor()

#CRUD

cursor.close()
conexao.close()

#CREATE
'''nome_prod = "chocolate"
valor = 15
comando = f'INSERT INTO vendas VALUES (DEFAULT, "{nome_prod}", {valor})'
cursor.execute(comando)
conexao.commit()'''

#READ
'''comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)'''

#UPDATE
'''nome_prod = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_prod = "{nome_prod}" '
cursor.execute(comando)
conexao.commit()'''

#DELETE

'''nome_prod = "todynho"
comando = f'DELETE FROM vendas WHERE nome_prod = "{nome_prod}" '
cursor.execute(comando)
conexao.commit()'''