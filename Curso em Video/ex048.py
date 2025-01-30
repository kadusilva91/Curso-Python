# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intrevalo de 1 e 500.

soma = 0
cont = 0
for c in range(1, 500, 2):
    if c %3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é de {soma}')