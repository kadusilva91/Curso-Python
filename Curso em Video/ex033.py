# Faça um programa que leie três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

