Nome = str(input('Qual é seu nome? '))
if Nome == 'Gustavo':
    print('Que nome bonito!')
elif Nome == 'Pedro' or Nome == "Maria" or Nome == "Paulo":
    print('Seu nome é bem popular no Brasil!')
elif Nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(Nome))