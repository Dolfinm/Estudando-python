lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis
print(lanche[-1]) #[1:3] [2:]

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont] na posição {cont}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(len(c))
print(c.count(5)) #vezes que aparece
print(c.index(2)) #primeravez que aparece

pessoa = ('Gustavo', 39, 'M', 99.88)
#del(pessoa[0]) nao funciona
print(pessoa)