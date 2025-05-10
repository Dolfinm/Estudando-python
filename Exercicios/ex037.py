#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('''1 - binário
2 - octal
3 - hexadecimal''')
Num = int(input('Escolha um número qualquer: '))
Conversao = int(input('Escolha qual será a base de conversão: '))
if Conversao == 1:
    print('O número {} em binário é {}'.format(Num, bin(Num)[2:]))
elif Conversao == 2:
    print('O número {} em binário é {}'.format(Num, oct(Num)[2:]))
elif Conversao == 3:
    print('O número {} em binário é {}'.format(Num, hex(Num)[2:]))
else: 
    print('Opção inválida. Tente novamente.')
                                                
