#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Numero = int(input('Digite um número de 0 a 9999: ').strip())
Unidade = Numero // 1 % 10
Dezena = Numero // 10 % 10
Centena = Numero // 100 % 10
Milhar = Numero // 1000 % 10
print('Casa das unidades: {}'.format(Unidade))
print('Casa das dezenas: {}'.format(Dezena))
print('Casa das centenas: {}'.format(Centena))
print('Casa das milhares: {}'.format(Milhar))

#n = int(input('Digite um número entre 0 e 9999: '))
#n2 = str(int(10000 + n))
#print('O número {} possui, {} milhares.'.format(n, n2[1]))
#print('O número {} possui, {} centenas. '.format(n, n2[2]))
#print('O número {} possui, {} dezenas. '.format(n, n2[3]))
#print('O número {} possui, {} unidades.'.format(n, n2[4]))