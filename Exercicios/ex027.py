# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Nome = input('Qual o seu nome? ').strip().title().split()
Pnome = Nome[0]
Unome = Nome[-1]
print('Seu primeiro nome é {}'.format(Pnome))
print('e seu último nome é {}'.format(Unome))

