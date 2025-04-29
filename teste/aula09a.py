frase = 'Curso em Vídeo Python'
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])

# ''' ''' pega o texto em varias linhas de uma vez

print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))

#frase = frase.replace('Python', 'Android')) da pra fazer uma atribuição

print('Curso' in frase)
print(frase.find('Curso'))
# -1 para resultados nao encontrados

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])