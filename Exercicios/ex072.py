#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
Resposta = 'S'
Numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treza', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while Resposta == 'S':
    if Resposta != 'S':
        break
    while True:
        Escolha = int(input('Escolha um número de 0 a 20 para aparecer pro extenso: '))
        if 0 <= Escolha <= 20:
            break
        print('Tente novamente. ', end='')
    print(Numeros[Escolha])
    Resposta = input('Quer continuar? [S/N] ').strip().upper()


