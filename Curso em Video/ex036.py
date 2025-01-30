#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = (casa*2) / (anos*12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ',end='')
print(f'a prestação será de {parcela:.2f}')
if parcela <= salario*0.30:
    print(f'Emprestimo APROVADO')
else:
    print(f'Emprestimo REPROVADO')
