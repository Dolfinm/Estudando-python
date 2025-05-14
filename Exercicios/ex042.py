# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

LadoA = float(input('Qual o comprimento do lado A? '))
LadoB = float(input('Qual o comprimento do lado B? '))  
LadoC = float(input('Qual o comprimento do lado C? '))
if LadoA < LadoB + LadoC and LadoB < LadoA + LadoC and LadoC < LadoA + LadoB:
    print('O triangulo pode ser formado!')
    if LadoA != LadoB and LadoB != LadoC and LadoA != LadoC:
        print('O triângulo é escaleno')
    elif LadoA == LadoB and LadoB == LadoC and LadoA == LadoC:
        print('O triângulo é equilátero')
    else:
        print('O triangulo é isosceles')
else:
    print('O triangulo não pode ser formado :(')