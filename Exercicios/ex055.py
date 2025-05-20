#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
Maior = 0
Menor = float('inf') #numero infinito
for pessoa in range(1, 6):
    Peso = float(input('Qual o peso do {}o individuo? '.format(pessoa)))
    if Peso > Maior:
        Maior = Peso
    if Peso < Menor:
        Menor = Peso
print('O maior peso lido foi de {}Kg'.format(Maior))
print('O menor peso lido foi de {}Kg'.format(Menor))