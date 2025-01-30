# Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final, de acordo com média atingida:

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1+n2) / 2
print(f'Tirando {n1} e {n2} sua média é {med:.1f}')
if med >= 7:
    print(f'O aluno esta APROVADO!')
elif med < 5:
    print(f'O aluno esta de REPROVADO')
else:
    print(f'O aluno enta de RECUPERACÃO')
