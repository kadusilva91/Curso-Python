# Faça um programa que leia o nome completo de uma pessoa. Mostrando em segui o primeiro e o ultimo nome separadamente

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
