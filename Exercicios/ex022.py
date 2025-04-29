#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

Nome = input('Qual é o seu nome? ').strip()
Maiusc = Nome.upper()
Minusc = Nome.lower()
NumCar = Nome.replace(' ','')
Letras = len(NumCar)
PrimNome = Nome.split()
PrimLetras = len(PrimNome[0])
print('Seu nome em maiúsculas é {}'.format(Maiusc))
print('Seu nome em minúsculas é {}'.format(Minusc))
print('Seu nome tem ao todo {} letras'.format(Letras))
print('Seu primeiro nome é {[0]} e ele tem {} letras'.format(PrimNome, PrimLetras))
