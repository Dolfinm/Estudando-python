#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

Preco = float(input('Qual o preço do produto a ser pago: R$'))
Metodo = int(input('''1 - Dinheiro/cheque
2 - Cartão
Qual o modo de pagamento? '''))
if Metodo == 1:
    print('Você recebeu 10% de desconto e pagará R${:.2f}'.format(Preco * 90/100))
elif Metodo == 2:
    Parcelas = int(input('Em quantas vezes gostaria de parcelar? '))
    if Parcelas == 1:
        print('Voce recebeu 5% de desconto e pagará R${:.2f}'.format(Preco * 95/100))
    elif Parcelas == 2:
        print('Voce pagará duas parcelas de R${:.2f}, em um total de R${:.2f}'.format((Preco/Parcelas), Preco))
    else:
        print('Voce pagará {} parcelas com 20% de juros de R${:.2f}, em um total de R${:.2f}'.format(Parcelas, (Preco/Parcelas*1.20), Preco*1.20))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')

        