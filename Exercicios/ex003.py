#Crie um programa que leia dois números e mostre a soma entre eles.


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre \033[0;30m{0} \033[me \033[0;30m{1} \033[mvale \033[0;32m{2}'.format(n1, n2, s))
