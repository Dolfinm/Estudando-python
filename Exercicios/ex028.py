#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
Computador = random.randrange(6)
Player = int(input('Tente descobrir o número escolhido pelo computador de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if Computador == Player:
    print('Parabéns, o número era {} e você acertou!'.format(Computador))
else:
    print('Poxa, você perdeu! O número era {}'.format(Computador))