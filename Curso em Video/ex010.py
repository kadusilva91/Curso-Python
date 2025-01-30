#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#considere U$$1,00 = R$3,27

real = float(input("Digite o valor que voce tem em Real R$: "))
dolar = real / 3.27
print(f"Levando em conta a cotação atual do dolar que esta em U$$ 5,35, voce pode comprar {dolar:.2f}U$$")
