# Crie um programa que leia dois valores e mostre um menu na tela: Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>>> Qual é a sua opção: '))
    if opcao == 1:
        resultado = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {resultado}')
    elif opcao == 2:
        resultado = n1 + n2
        print(f'O resultado de {n1} * {n2} é igual a {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    sleep(2)
print('Fim do programa! Volte sempre!')
