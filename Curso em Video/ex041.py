# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import date

nasc = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Cassifiação: MIRIM')
elif idade <=14:
    print('Cassifiação: INFANTIL')
elif idade <=19:
    print('Cassifiação: JUNIOR')
elif idade <=25:
    print('Cassifiação: SÊNIOR')
else:
    print('Classificação: MASTER')
