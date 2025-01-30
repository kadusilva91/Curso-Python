#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área 
# e a quantidade de tinta necessária para pinta-la 
# sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
litros = area / 2
print(f"Esta parede tem a área de {area:.2f}m², e será necessário {litros:.2f}litros de tinta")
