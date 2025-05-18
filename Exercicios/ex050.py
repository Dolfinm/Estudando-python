#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
Soma = 0
for c in range(0, 6):
    N = int(input('Insira um número inteiro: '))
    if N % 2 == 0:
        Soma = Soma + N
print('A soma dos números pares é igual a {}'.format(Soma))
