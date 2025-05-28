#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
Computador = random.randrange(11)
Player = 11
Tentativas = 0
while Player != Computador:
    Player = int(input('Tente descobrir o número escolhido pelo computador de 0 a 10: '))
    if Computador != Player:
        if Computador > Player:
            print('Mais... tente mais uma vez')
            Tentativas = Tentativas + 1
        else: 
            print('Menos... tente mais uma vez')
            Tentativas = Tentativas + 1

print('Parabéns! Você acertou o número {} depois de {} tentativas'.format(Computador, Tentativas+1))