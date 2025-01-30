#Escreva um programa que pergunte a quantidade de Km percorridos por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodade.

dias = int(input("Quantos dias alugados?: "))
Km = float(input("Quantos Km rodados?: "))
total = (dias * 60) + (Km * 0.15)
print(f"O total a pagar é de R${total:.2f}")