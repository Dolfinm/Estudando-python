# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
LadoA = float(input('Qual o comprimento do lado A? '))
LadoB = float(input('Qual o comprimento do lado B? '))  
LadoC = float(input('Qual o comprimento do lado C? '))
if LadoA < LadoB + LadoC and LadoB < LadoA + LadoC and LadoC < LadoA + LadoB:
    print('O triangulo pode ser formado!')
else:
    print('O triangulo não pode ser formado :(')