#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
N = float(input('Digite um número: '))
print('Sua porção inteira é {}'.format(math.trunc(N)))