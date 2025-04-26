# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
A1 = input('Primeiro aluno: ')
A2 = input('Segundo aluno: ')
A3 = input('Terceiro aluno: ')
A4 = input('Quarto aluno: ')
Sorteio = random.choice([A1, A2, A3, A4])
print('O aluno sorteado para apagar o quadro será {}'.format(Sorteio))
