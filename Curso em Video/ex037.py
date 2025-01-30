# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
print('[ 1 ] converter para BINÁRIO
print('[ 2 ] converter para OCTAL
print('[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{n} convertido em BINÁRIO é igual a', bin(n)[2:])
elif opcao == 2:
    print(f'{n} convertido em OCTAL é igual a', oct(n)[2:])
elif opcao == 3:
    print(f'{n} convertido em HEXADECIMAL é igual a', hex(n)[2:])
else:
    print('Opção invalida. Tente novamente.')
