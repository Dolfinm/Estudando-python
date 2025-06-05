# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
multiplo = tabuada = 1
while multiplo >= 0: 
    multiplo = int(input('Quer ver a tabuada de qual valor? '))
    if multiplo < 0:
        break
    print ('-' * 25)
    if tabuada == 11:
        tabuada -= 10
    while tabuada < 11:
        resposta = multiplo * tabuada
        print(f'{multiplo} x {tabuada} = {resposta}')
        tabuada += 1
    print ('-' * 25)
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')