# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (c*n)))