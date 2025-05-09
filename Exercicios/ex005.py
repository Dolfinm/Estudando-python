#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
suc = n + 1
ant = n - 1
print('\033[0;32m{} \033[mtem como antecessor \033[0;33m{} \033[me como sucessor \033[0;34m{}\033[m'.format(n, ant, suc))