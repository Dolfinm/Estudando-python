#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

Nome = input('Qual o seu nome? ').strip().upper().split()
Silva = 'SILVA' in Nome
print('{} tem Silva no nome? {}'.format(Nome, Silva)) 
