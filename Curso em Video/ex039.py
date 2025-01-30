# Escreva um programa que leia a o ano de nascimento de um jovem e informe, de que acordo com a sua idade, ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
if idade > 18:
    ano_alist = idade - 18
    print(f'Você ja deveria ter se alistado há {ano_alist} anos.')
    print(f'Seu alistamento foi em {ano_atual-ano_alist}')
elif idade < 18:
    ano_alist = 18 - idade
    print(f'Ainda faltam {ano_alist} anos para o seu alistamento.')
    print(f'Seu alistamento será em {ano_atual + ano_alist} ')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
