#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500
sum = 0
for c in range(1, 500):
    if c % 2 == 1:
        if c % 3 == 0:
            sum = sum + c
print(sum)