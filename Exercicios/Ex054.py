#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
Maidade = 0
Meidade = 0
atual = date.today().year
for c in range(1,8):
    Nascimento = int(input('Em que ano a {}a pessoa nasceu? '.format(c)))
    Idade = atual - Nascimento
    if Idade >= 21:
        Maidade = Maidade + 1
    else:
        Meidade = Meidade + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(Maidade))
print('E também tivemos {} pessoas menores de idade'.format(Meidade))

