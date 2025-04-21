nome = input('Qual é o seu nome? ')
print('Praze em te conhecer {:=^20}!'.format(nome))

#usa > para deslocar a direita e < a esquerda e um caractere para preencher o espaço restante

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e \n a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisao inteira é {} e potência é {}'.format(di, e))