#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Np = int(input('Insira um número inteiro: '))
primo = 0
for c in range(1, Np+1):
    if Np % c == 0:
        print('\033[0;32m{}\033[m'.format(c), end=' ')
        primo = primo + 1
    else:
        print('{}'.format(c), end=' ')
if primo == 2:
    print(', logo {} é um número primo e é divisivel por {} numeros!'.format(Np, primo))
else:
    print(', logo {} não é primo e é divisivel por {} numeros!'.format(Np, primo))