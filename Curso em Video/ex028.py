# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça ao usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
player = int(input('Em qual número em pensei? '))
print('PROCESSANDO...')
sleep(3)
print(f'Voce escolheu o número {player}')
if player == pc:
    print('Parabéns, você acertou')
else:
    print(f'Você errou, eu pensei no número {pc}')
