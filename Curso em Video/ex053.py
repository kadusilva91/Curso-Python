# Crie um programa que leia uma frase qualquer e diga se ela á um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: 'Apos a sopa' ' A sacada da casa' 'A torre da derrota' 'O lobo ama o bolo'

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos uma palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
    