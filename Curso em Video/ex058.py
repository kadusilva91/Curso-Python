# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pc = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais um vez.')
        else:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {palpites} palpites. Parabéns!')
