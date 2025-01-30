#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira Ex digite '6.127' tem a parte inteira '6'

from math import floor
num = float(input('Digite um número real: '))
numInt = floor(num)
print(f'O número real {num}, se torna {numInt}')
