# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
Nascimento = int(input('Qual o seu ano de nascimento? '))
Ano = datetime.date.today().year
print ('Quem nasceu em {} tem {} em {}'.format(Nascimento, (Ano-Nascimento), Ano))
if Ano - Nascimento == 18:
    print('Você fará 18 anos e está na hora de se alistar!')
elif  Ano - Nascimento > 18:
    print('Você já tem mais de 18 anos e seu tempo de alistamento ja passou')
    print('Seu alistamento foi em {} a {} ano(s)'.format((Nascimento+18), (Ano-Nascimento-18)))
else:
    print('Voce ainda é menor de idade e ainda irá se alistar quando fizer 18 anos.')
    print('Seu alistamento séra em {} e ainda faltam {} ano(s)'.format((Nascimento+18), Nascimento-Ano+18))