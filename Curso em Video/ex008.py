#Escreva um programa que escreva um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input("Digite o valor em metros para a conversão: "))
cm = m * 100
ml = m * 1000
print(f"{m}m é igual a {cm:.0f}cm e {ml:.0f}ml ")
