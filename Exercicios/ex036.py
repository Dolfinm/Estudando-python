#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

Emprestimo = float(input('Qual o valor da casa? R$'))
Salario = float(input('Qual o valor do seu salário? R$'))
Tempo = int(input('Em quanto anos irá ser feito o pagamento: '))
if Emprestimo / (Tempo*12) < Salario * (30/100):
    print('A prestãção mensal será de {:.2f} e a compra da casa será efetuada'.format(Emprestimo / (Tempo*12)))
else:
    print('A prestação será de {:.2f} e excede 30% do salário e não poderá ser efetuada'.format(Emprestimo / (Tempo*12)))