#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

Cidade = input('Insira o nome da cidade: ').strip()
CidadeU = Cidade.upper()
CidadeUS = CidadeU.split()
Santo = 'SANTO' in CidadeUS[0][:5]
print('A cidade começa com o nome Santo? {}'.format(Santo))
