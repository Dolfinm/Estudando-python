#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
Velocidade = float(input('Qual é a velocidade do carro? '))
if Velocidade <= 80:
    print('A velocidade é de {} e está dentro do limite, pode prosseguir normalmente!'.format(Velocidade))
else:
    Multa = (Velocidade - 80) * 7
    print('Essa velocidade ultrapassa o limite de 80Km/h e recebá uma multa de R${:.2f}'.format(Multa))