#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
N1 = float(input('Insira a primeira nota: '))
N2 = float(input('Insira a segunda nota: '))
M = (N1+N2)/2
Media = round(M, 1) 
if Media < 5.0:
    print('A média entre {} e {} é {} e o aluno foi reprovado'.format(N1, N2, Media))
elif 5.0 <= Media <= 6.9:
    print('A média entre {} e {} é {} e o aluno foi posto em recuperação'.format(N1, N2, Media))
else:
    print('A média entre {} e {} é {} e o aluno foi aprovado'.format(N1, N2, Media))