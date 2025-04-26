#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Qual o valor do cateto aposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hip = math.sqrt(ca ** 2 + co ** 2)
print('O valor da hipotenusa com cateto oposto valendo {} e cateto adjacente valendo {} é de {:.2f}'.format(co, ca, hip))
 
 #math.hypot(co, ca)