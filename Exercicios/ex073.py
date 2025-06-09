''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Grêmio.'''
TabelaTimes = ("Flamengo", "Cruzeiro", "Bragantino", "Palmeiras", "Fluminense", "Botafogo", "Bahia", "Mirassol", "Atlético-MG", "Ceará", "Corinthians", "Grêmio", "São Paulo", "Internacional", "Vasco", "Vitória", "Fortaleza", "Santos", "Juventude", "Sport")
print('=-' * 20)
print('Lista de times do Brasileirão:', TabelaTimes)
print('=-' * 20)
print('Os 5 primeiros são', TabelaTimes[:5])
print('=-' * 20)
print('Os 4 últimos são', TabelaTimes[-4:])
print('=-' * 20)
print('Times em ordem alfabética:', sorted(TabelaTimes))
print('=-' * 20)
print(f'O Grêmio está na {TabelaTimes.index('Grêmio')+1}° posição')

'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont] na posição {cont}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''