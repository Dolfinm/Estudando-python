# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

import datetime
Nascimento = int(input('Qual o seu ano de nascimento? '))
Ano = datetime.date.today().year
Idade = Ano - Nascimento
print('O atleta tem anos {}'.format(Idade))
if Ano <= 9:
    print('Você pertence a categoria MIRIM')
elif 9 < Idade <= 14 :
    print('Você pertence a categoria INFANTIL')
elif 14 < Idade <= 19 :
    print('Você pertence a categoria JÚNIOR')
elif 19 < Idade <= 25:
    print('Você pertence a categoria SÊNIOR')
else:
    print('Você pertence a categoria MASTER')
