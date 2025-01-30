# Crie um programa que leie o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: Qual é o total na compra. Quantos produtos custam mais de R$1000. Qual é o nome do produto mais barato.


total = tot1000 = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f"{'FIM DO PROGRAMA':-^40}")
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {tot1000} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi a(o){barato} que custa R${menor:.2f}')
