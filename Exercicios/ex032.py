#Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 
# De 4 em 4 anos é ano bissexto.
#De 100 em 100 anos não é ano bissexto.
#De 400 em 400 anos é ano bissexto.
#Prevalecem as últimas regras sobre as primeiras.
import datetime
Ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if Ano == 0:
    Ano = datetime.date.today().year
if Ano % 400 == 0:
    print('O ano {} é bissexto!'.format(Ano))
else:
    if Ano % 4 == 0 and Ano % 100 != 0:
        print('O ano {} é bissexto!'.format(Ano))
    else:
        print('O ano {} não é bissexto!'.format(Ano))