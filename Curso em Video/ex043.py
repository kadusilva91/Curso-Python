# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
peso = float(input('Qual é o seu peso (Kg) '))
altura = float(input('Qual é a sua altura (m) '))
imc = peso / (altura **2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif imc <= 25:
    print('Parabêns, você esta na faixa PESO NORMAL')
elif imc <= 30:
    print('Você esta em SOBREPESO')
elif imc <= 40:
    print('Você esta em OBESIDADE')
else:
    print('Você esta em OBESIDADE MÓRBIDA, cuidado!')