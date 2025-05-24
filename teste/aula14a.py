'''for c in range(1, 10):
    print(c)
print('Fim')'''

c = 1
while c < 10:
    print(c)
    c = c + 1
ProcessLookupError
print('fim')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    num = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]  ')).upper()
print('Fim')

numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))
    if n != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par, impar))


