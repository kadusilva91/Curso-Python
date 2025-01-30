#Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço de um produto: "))
desconto = preco * 0.95
print(f"O produto com 5% de desconto fica {desconto:.2f}R$")
