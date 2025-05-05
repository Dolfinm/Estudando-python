#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

Distancia = float(input('Qual foi a distância da viagem? '))
if Distancia <= 200: 
    preco = Distancia * 0.50
    print('O preço da passagem da viagem de {}Km é de R${:.2f}'.format(Distancia, preco))
else: 
    preco = Distancia * 0.45
    print('O preço da passagem da viagem de {}Km é de R${:.2f}'.format(Distancia, preco))
