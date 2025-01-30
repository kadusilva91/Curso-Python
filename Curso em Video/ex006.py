#Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um valor e descubra o seu dobro, triplo e sua raiz quadrada "))
dob = n*2
tri = n*3
raiz = n**(1/2)
print(f"O dobro de {n} é {dob},\no triplo é {tri},\ne a raiz quadrada é {raiz:.1f} !")
