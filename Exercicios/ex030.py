#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
N = int(input('Insira um número qualquer: '))
if N % 2 == 1:
    print('O número {} é impar!'.format(N))
else: 
    print('O número {} é par!'.format(N))