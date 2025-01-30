# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
v = 0
while True:
    pc = randint(0, 10)
    n = int(input('Diga um  número: '))
    total = n + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador {pc}. Total de {total} ', end='')
    print('DEU PAR' if total %2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total %2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')