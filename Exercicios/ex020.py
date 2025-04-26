#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
A1 = input('Primeiro aluno: ')
A2 = input('Segundo aluno: ')
A3 = input('Terceiro aluno: ')
A4 = input('Quarto aluno: ')
Sorteio = [A1, A2, A3, A4]
random.shuffle(Sorteio)
print('A ordem sorteada foi {}'.format(Sorteio))
