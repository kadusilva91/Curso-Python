#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Qual o salário atual do funcionário: "))
aumento = salario * 0.15
novosala = salario * 1.15
print(f"O salário atual de {salario:.2f}R$ com um aumento de {aumento:.2f}R$ equivalente a 15% \nVai para {novosala:.2f}R$ ")
