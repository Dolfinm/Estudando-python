# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

SalarioAtual = float(input('Qual o salário atual do funcionário? R$'))
if SalarioAtual > 1250:
    SNovo = SalarioAtual * 1.10
    print('O aumento de 10% fez o salário aumentar para R${:.2f}'.format(SNovo))
else:
    SNovo = SalarioAtual * 1.15
    print('O aumento de 15% fez o salário aumentar para R${:.2f}'.format(SNovo))