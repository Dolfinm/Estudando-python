#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O numero {}, tem como dobro {}, como triplo {} e como raiz quadrada {:.3f}'.format(n, d, t, rq))

# x ** y = pow(x, y)
