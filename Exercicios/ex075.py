# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
pares = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
if numeros % 2 == 0:
    pares += 1
print(f'Você difitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na {numeros.index(3)}° posição')
print(f'Os valores pares digitados foram {pares}')