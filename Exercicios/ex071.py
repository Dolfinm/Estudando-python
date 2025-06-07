'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('=' * 20)
print('       BANDO CEV')
print('=' * 20)
Saque = int(input('Que valor você quer sacar? R$'))
if (Saque / 50) > 1:
    Saque50 = Saque // 50
    Resto = Saque - Saque50 * 50
    print(f'Total de {Saque50} cédulas de R$50')
if (Resto / 20) > 1:
    Saque20 = Resto // 20
    Resto = Resto - Saque20 * 20
    print(f'Total de {Saque20} cédulas de R$20')
if (Resto / 10) > 1:
    Saque10 = Resto // 10
    Resto = Resto - Saque10 * 10
    print(f'Total de {Saque10} cédulas de R$10')
if (Resto / 1) > 1:
    Saque1 = Resto // 1
    Resto = Resto - Saque1 * 1
    print(f'Total de {Saque1} cédulas de R$1')
print('=' * 20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

