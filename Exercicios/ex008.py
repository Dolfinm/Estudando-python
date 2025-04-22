#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Insira a quantidade de metros: '))
cm = m * 100
mm = m * 1000
print('{} metros são iguais a {} centimetros que são iguais a {} milimetros'.format(m, cm, mm))