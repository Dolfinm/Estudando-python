#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

Caractere = (input('Digite algo: '))
print('O \033[0;30mtipo primitivo \033[mdesse valor é', type(Caractere))
print('Só tem \033[0;31mespaços\033[m?', Caractere.isspace())
print('É um \033[0;32mnúmero\033[m?', Caractere.isnumeric())
print('É \033[0;33malfabético\033[m?', Caractere.isalpha())
print('É \033[0;34malfanumérico\033[m?', Caractere.isalnum())
print('Está em \033[0;35mmaiúsuculas\033[m?', Caractere.isupper())
print('Está em \033[0;36mminúsculas\033[m?', Caractere.islower())
print('Está \033[1;37mcapitalizada\033[m?', Caractere.istitle())




