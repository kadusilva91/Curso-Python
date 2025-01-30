# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço de for

n = int(input('Digite um número para ver a sua tabuada: '))
print(f"A TABUADA DO NÚMERO {n}")
for c in range(1,11):
    print(f'{n} x {c} = {n*c}')