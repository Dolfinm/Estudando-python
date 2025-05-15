# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('Vamos calcular seu IMC!')
Peso = float(input('Insira seu peso em quilos: '))
Altura = float(input('Insira a sua altura em metros: '))
IMC = Peso / Altura ** 2
if IMC < 18.5:
    print('Seu IMC é {:.2f}, voce está abaixo do peso'.format(IMC))
elif 18.5 <= IMC < 25:
    print('Seu IMC é {:.2f}, voce está no peso ideal'.format(IMC))
elif 25 <= IMC < 30:
    print('Seu IMC é {:.2f}, voce está com sobrepeso'.format(IMC))
elif 30 <= IMC < 40:
    print('Seu IMC é {:.2f}, voce está com Obesidade'.format(IMC))
else:
    print('Seu IMC é {:.2f}, voce está com obesidade mórbida'.format(IMC))