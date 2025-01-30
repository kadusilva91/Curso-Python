# Crie um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra A
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra A aparece na posição {frase.find("A")+1}')
print(f'A ultima letra A aparece na posição {frase.rfind("A")+1}')
