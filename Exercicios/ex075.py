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
print(f'Você difitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição')
else:
    print('O valor 3 não aparece em nenhuma posição')
print('Os valroes pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

'''
valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')'''