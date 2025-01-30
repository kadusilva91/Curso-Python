 # Faça um program que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompidoquando o número solicitado for negativo.

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*35)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')