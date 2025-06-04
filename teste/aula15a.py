n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos.') #Python 3.6+
print('O %s tem %d anos' % (nome, idade)) #Python 2
