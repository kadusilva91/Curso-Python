# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostres: a média de idade do grupo, qual é o nome do mais velho e quantas mulheres tem menos de 20 anos.

media = 0
somaidade = 0
maioridadehomem = 0
nomevelho =''
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade / 4
print (f'A média de idade do grupo é de {media} anos')
print (f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print (f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
