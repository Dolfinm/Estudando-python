#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
Palavras = ('aprender', 'programar', 'linguagem', 'python',
'curso', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in Palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end =' ')

#nao entendi bosta