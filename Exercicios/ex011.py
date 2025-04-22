#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 

L = float(input('Largura da parede: '))
H = float(input('Altura da parede: '))
B = (L*H)/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m^2'.format(L, H, (L*H)))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(B))
