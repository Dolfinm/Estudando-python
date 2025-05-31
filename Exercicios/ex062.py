#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
c = 0
print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while c < 10:
    print(n1, end=' -> ')
    n1 = n1 + razao
    c = c + 1
    if c == 10:
        Mtermo = int(input('''
Quer adicionar quantos termos a mais: '''))
        c = c - Mtermo 
print('Fim')