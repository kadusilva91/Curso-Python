# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} número(s) pare(s) e a soma foi {soma}')
