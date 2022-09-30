# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alinhamento.

import datetime

anoNascimento = int(input('Informe qual o seu ano de nascimento: '))

dataAtual = datetime.date.today()
anoAtual = dataAtual.year
idade = anoAtual - anoNascimento

if idade < 18:
    print(f'Você ainda irá se alistar! Tens somente {idade} anos. Faltam {18-idade} anos para se alistar!')
elif idade == 18:
    print(f'Já é hora de se alistar! Você tem {idade} anos!')
else:
    print(f'Você já passou da idade! Tens {idade} anos. Você deveria ter se alistado há {idade - 18} anos!')