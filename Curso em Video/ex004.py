#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ela

a = input("Digite algo ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print("É numérico? ", a.isnumeric())
print("É alfanumérico ", a.isalnum())
print("Esta em maiúsculas? ", a.isupper())
print("Esta em minúsculas? ", a.islower())
print("Esta capitalizada? ", a.istitle())
