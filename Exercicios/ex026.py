#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Escreva uma frase: ').strip().lower()
ases = frase.count('a')
print('Há {} A na frase'.format(ases))
print('{} é a posição no qual A aparece pela ultima vez'.format(frase.find('a')+1))
print('{} é a posição no qual A primeira vez pela ultima vez'.format(frase.rfind('a')+1))
