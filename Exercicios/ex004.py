#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

Caractere = (input('Digite algo: '))
print('O tipo primitivo desse valor é', type(Caractere))
print('Só tem espaços?', Caractere.isspace())
print('É um número?', Caractere.isnumeric())
print('É alfabético?', Caractere.isalpha())
print('É alfanumérico?', Caractere.isalnum())
print('Está em maiúsuculas?', Caractere.isupper())
print('Está em minúsculas?', Caractere.islower())
print('Está capitalizada?', Caractere.istitle())




