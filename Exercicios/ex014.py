#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

C = float(input('Qual é a temperatura em C°? '))
F = C * 1.8 + 32
print('A tempertatura em Fahrenheit seria de {}F°'.format(F))