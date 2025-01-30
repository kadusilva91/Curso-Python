# Faça um programa que faça o computador jogar jokempô com você.

from  random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
play = int(input('Qual é a sua jogada? '))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-='*11)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[play]}')
print('-='*11)
if pc == 0:
    if play == 0:
        print('EMPATE')
    elif play == 1:
        print('JOGADOR VENCE')
    elif play == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:
    if play == 0:
        print('COMPUTADOR VENCE')
    elif play == 1:
        print('EMPATE')
    elif play == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if play == 0:
        print('JOGADOR VENCE')
    elif play == 1:
        print('COMPUTADOR VENCE')
    elif play == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')