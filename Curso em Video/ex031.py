# Desenvolver um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = float(input('Qual é a distância da sua viagem? '))
print(f'Você esta preste a começar uma viagem de {viagem}Km')
if viagem > 200:
    preco = (viagem * 0.45)
else:
    preco = (viagem * 0.50)
print(f'E o preço da sua passagem será de R${preco:.2f}')
print('FAÇA UMA ÓTIMA VIAGEM...')
