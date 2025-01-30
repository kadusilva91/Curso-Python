# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final mostre os 10 primeiros termos dessa progressão.

print("="*25)
print('  10 TERMOS DE UMA PA ')
print("="*25)

t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
for c in range(t, d+r, r):
    print(c,end=' -> ')
print('ACABOU')
