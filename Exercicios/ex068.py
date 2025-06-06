#: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
Perdeu = Ganhou = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while Perdeu < 1:
    if Perdeu == 1:
        break
    Player = int(input('Diga um valor: '))
    ParouImpar = (input('Par ou Ímpar? [P/I] ')).strip().upper()
    Bot = random.randrange(10)+1 
    if ParouImpar == 'P':
        if (Player + Bot) % 2 == 0:
            Ganhou += 1
            print('=-' * 20)
            print('Voce jogou {} e o computador {}. Total de {} DEU PAR'.format(Player, Bot, (Player+Bot)))
            print('=-' * 20)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        elif (Player + Bot) % 2 == 1: 
            Perdeu += 1
            print('=-' * 20)
            print('Voce jogou {} e o computador {}. Total de {} DEU IMPAR'.format(Player, Bot, (Player+Bot)))
            print('=-' * 20)
    elif ParouImpar == 'I':
        if (Player + Bot) % 2 == 1:
            Ganhou += 1
            print('=-' * 20)
            print('Voce jogou {} e o computador {}. Total de {} DEU IMPAR'.format(Player, Bot, (Player+Bot)))
            print('=-' * 20)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        elif (Player + Bot) % 2 == 0: 
            Perdeu += 1
            print('=-' * 20)
            print('Voce jogou {} e o computador {}. Total de {} DEU PAR'.format(Player, Bot, (Player+Bot)))
            print('=-' * 20)
print('Você PERDEU!')
print('=-' * 20)
print('GAME OVER! Você venceu {} vezes'.format(Ganhou))
    
    

    

