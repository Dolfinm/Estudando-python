#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
NMaior = 0
NMenor = float('inf')
Resp = 'S'
TotN = 0
Vezes = 0
while Resp == 'S':
    N = int(input('Digite um número: '))
    if N > NMaior:
        NMaior = N
    elif N < NMenor:
        NMenor = N
    TotN += N
    Vezes += 1
    Resp = input('Quer Continuar? [S/N] ').strip().upper()
print('Você digitou {} números e a média foi {:.2f}'.format(Vezes, (TotN/Vezes)))
print('O menor número digitado foi {} e o maior foi {}'.format(NMenor, NMaior))
