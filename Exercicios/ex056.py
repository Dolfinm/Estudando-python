#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
TotIdade = 0
Fnova = 0
Mvelho = 0
for pessoa in range(1, 5):
    Nome = str(input('Insira o nome da {}a pessoa: '.format(pessoa))).title().strip()
    Idade = int(input('Insira a idade da {}a pessoa: '.format(pessoa)))
    Sexo = str(input('Insira o sexo da {}a pessoa [F ou M]: '.format(pessoa))).upper().strip()
    TotIdade = TotIdade + Idade
    if Sexo == 'M':
        if Idade > Mvelho:
            Mvelho = Idade 
            NomeMvelho = Nome
    else:
        if Idade < 20:
            Fnova = Fnova + 1
MediaIdade = TotIdade/4
print('A média da idade do grupo é {:.2f} anos'.format(MediaIdade))
print('O {} é o homem mais velho com {} anos'.format(NomeMvelho, Mvelho))
print('Ao todo são {} mulheres menores de 20 anos'.format(Fnova))
