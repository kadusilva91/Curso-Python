# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, do zero ao vinte. Seu programa deve ler um número pelo teclado (entre  0 e 20) e mostralo por extenso.
cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente ', end='')
print(f'Você digitou o número {cont[n]}')
