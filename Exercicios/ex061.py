# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
c = 0
print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while c < 10:
    print(n1, end=' -> ')
    n1 = n1 + razao
    c = c + 1
print('Fim')