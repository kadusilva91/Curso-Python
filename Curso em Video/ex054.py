# Crie um programa que leia a data de nascimento de 7 pessoas. No final mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.

from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    data = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = hoje - data
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade \nE também tivemos {menor} pessoas menores de idade')
