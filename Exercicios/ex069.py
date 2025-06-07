'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
Continuar = 'S'
TotHomem = Tot18 = MulherMenos20 = 0
while Continuar == 'S':
    if Continuar != 'S':
        break
    print('-' * 20)
    print('     CADASTRE UMA PESSOA')
    print('-' * 20)
    Idade = int(input('Idade: '))
    Sexo = (input('Sexo: [M/F] '))
    print('-' * 20)
    if Idade >= 18:
        Tot18 += 1
    if Sexo == "M":
        TotHomem += 1
    if Sexo == "F" and Idade < 20:
        MulherMenos20 += 1    
    Continuar = (input('Quer continuar? [S/N] ')).strip().upper()
print(f'Total de pessoas com mais de 18 anos: {Tot18}')
print(f'Ao todo temos {TotHomem} homens cadastrados')
print(f'e temos {MulherMenos20} mulheres com menos de 20 anos')


    