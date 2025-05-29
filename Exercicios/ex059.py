'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
Menu = 0
N1 = float(input('Insira o primeiro número: '))
N2 = float(input('Insira o segundo número: '))
while Menu != 5: 
    Menu = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
                     
'''))
    if Menu == 1:
        print('A soma é {}'.format(N1+N2))
    elif Menu == 2:
        print('O produto é {}'.format(N1*N2))
    elif Menu == 3:
        Maior = [N1, N2]
        Nmaior = max(Maior)
        print('O maior número é {}'.format(Nmaior))
    elif Menu == 4:
        N1 = float(input('Insira o primeiro número: '))
        N2 = float(input('Insira o segundo número: '))
    elif Menu > 5:
        print('Esta função não existe. Tente novamente.')
print('Até mais!')