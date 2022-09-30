# A Conferação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a
# idade.
# Até 9 anos: MIRiM
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: MASTER.
from time import sleep

print('-=-='*8)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-='*8)

idade = int(input('Informe a sua idade: '))

print('ANALISANDO...')
sleep(3)

if idade <= 9:
    print('Seja bem vindo! Você é da categoria MIRIM.')
elif 10 <= idade <= 14:
    print('Seja bem-vindo! Você é da categoria INFANTIL.')
elif 15 <= idade <= 19:
    print('Seja bem-vindo! Você é da categoria JUNIOR.')
else:
    print('Seja bem-vindo! Você é da categoria MASTER.')