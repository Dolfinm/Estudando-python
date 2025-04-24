#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

Sa = float(input('Qual o salário atual do funcionário? R$'))
Sn = Sa * 115/100
print('Com o reajuste, o novo salário com aumento de 15% será de R${:.2f}'.format(Sn))