# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
D = int(input('Durante quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km rodados? '))
S = D * 60 + Km * 0.15
print('O valor pago por {} dias de aluguel e {}Km rodados é de R${:.2f}'.format(D, Km, S))
