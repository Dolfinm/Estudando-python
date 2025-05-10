#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
Num1 = int(input('Escreva o primeiro número inteiro: '))
Num2 = int(input('Escreva o segundo número inteiro: '))
if Num1 > Num2: 
    print('O primeiro valor é maior')
elif Num1 == Num2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('O segundo valor é maior')