#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
Frase = str(input('Insiria uma frase qualquer: ')).replace(' ','').upper()
Palindromo = Frase[::-1]
if Frase == Palindromo:
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo.')
