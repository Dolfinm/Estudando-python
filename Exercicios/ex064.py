# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
c = 0
Soma = 0
TotC = 0
while c != 999:
    c = int(input('Digite um número [999 para parar]: '))
    if c != 999:
        Soma += c 
        TotC += 1
print('A soma de {} números digitados é {}'.format(TotC, Soma))