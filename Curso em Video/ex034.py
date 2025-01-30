# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
print(f'Quem ganhava R${salario:.2f}, passa a ganhar R${aumento:.2f}')
