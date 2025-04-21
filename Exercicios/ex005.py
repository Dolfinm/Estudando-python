#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
suc = n + 1
ant = n - 1
print('{} tem como antecessor {} e como sucessor {}'.format(n, ant, suc))