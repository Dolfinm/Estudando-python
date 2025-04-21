 #Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Qual foi a primeira nota do aluno? '))
n2 = float(input('E a segunda nota? '))
media = (n1 + n2) / 2
print('A média do aluno foi {:.f1}'.format(media))