'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
Continuar = 'S'
TotPreco = Produto1000 = 0
Pmaisbarato = float('inf')
print('-' * 40)
print('       LOJA SUPER BARATAO')
print('-' * 40)
while Continuar == 'S':
    if Continuar != 'S':
        break
    NomeP = input('Nome do produto: ').strip().title()
    PrecoP = float(input('Preço: R$'))
    Continuar = input('Quer continuar? [S/N] ').strip().upper()
    TotPreco += PrecoP
    if PrecoP > 1000:
        Produto1000 += 1
    if PrecoP < Pmaisbarato:
        Pmaisbarato = PrecoP
        Nomemaisbarato = NomeP
print('--------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi R${TotPreco:.2f}')
print(f'Temos {Produto1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {Nomemaisbarato} que custa R${Pmaisbarato:.2f}')


