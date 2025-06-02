#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
n = 0
proxTermo = 1
TermoAtual = 0
TermoAnterior = 0
c = int(input('Quantos elementos de uma sequência de fibonacci deseja ver? '))
while n < c:
    print('{}'.format(TermoAtual), end = ' -> ', )
    TermoAtual = proxTermo
    proxTermo = TermoAtual + TermoAnterior
    TermoAnterior = TermoAtual 
    n += 1
print('FIM!')