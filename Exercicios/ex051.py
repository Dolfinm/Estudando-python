# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
P1 = int(input('Qual o primeiro termo da P.A? '))
razao = int(input('Qual a razão? '))
for c in range(0, 10,):
    print('{}'.format(P1), end=' -> ')
    P1 = P1 + razao
print('ACABOU!')