"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No
início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

quantidade = int(input('VALOR DE SAQUE: '))
total = quantidade
cedula = 50
totalCedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break
print('CONFIRA O DINHEIRO SACADO.')