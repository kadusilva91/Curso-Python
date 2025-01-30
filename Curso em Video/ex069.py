# Crie um program que leai a idade e o sexo de várias pessoas. A cada pessoas cadastrada, o programa deve perguntar se o usuário quer ou não continuar. No final morte. Quantas pessoas tem mais de 18 anos. Quantos homens foram cadastrados. Quantas mulheres tem menos de 20 anos.
tot18 = totH = totM20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade < 20 and sexo == 'F':
        totM20 += 1
    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('ACABOU')
print(f'Total de pessoas com mais de 18: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')