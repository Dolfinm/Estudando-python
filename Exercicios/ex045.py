#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
Jogador = int(input('''Escolha: 
1 - Pedra
2 - Papel 
3 - Tesoura
'''))
Bot = random.randrange(3)+1
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if Jogador == Bot:
    print('Empate!')
else:
    if Jogador == 1 and Bot == 2:
        print('O bot escolheu papel e voce PERDEU!')
    elif Jogador == 1 and Bot == 3:
        print('O bot escolheu tesoura e voce GANHOU!')
    elif Jogador == 2 and Bot == 1:
        print('O bot escolheu Pedra e voce GANHOU!')
    elif Jogador == 2 and Bot == 3:
        print('O bot escolheu tesoura e voce PERDEU!')
    elif Jogador == 3 and Bot == 1:
        print('O bot escolheu pedra e voce PERDEU!')
    elif Jogador == 3 and Bot == 2:
        print('O bot escolheu papel e voce GANHOU!')
    
