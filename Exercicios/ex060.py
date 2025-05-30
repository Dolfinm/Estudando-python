#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
Fatorial = 1
c = int(input('Escolha um número para ver seu fatorial: '))
while c != 1:
    Fatorial = Fatorial * c
    c = c - 1
print(Fatorial)
