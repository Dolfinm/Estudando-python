#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
n3 = float(input('Insira o terceiro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print('O maior número é {} e o menor é {}'.format(maior, menor))