"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[0] - Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from os import system
from re import S
from time import sleep

system('cls')

primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))

print('=== ESCOLHA UMA DAS OPÇÕES ===')
print('[1] - Somar. \n[2] - Multiplicar. \n[3] - Maior \n[4] - Novos números. \n[0] - Sair.')

opcao = int(input('Digite a sua opção: '))

while opcao != 0:
    if opcao > 4:
        print('Esta opção não é valida!')
        sleep(1)
        system('cls')
        print('=== ESCOLHA UMA DAS OPÇÕES ===')
        print('[1] - Somar. \n[2] - Multiplicar. \n[3] - Maior \n[4] - Novos números. \n[0] - Sair.')
        opcao = int(input('Digite a sua opção: '))
    if opcao == 1: # Somar os valores.
        soma = primeiroNumero + segundoNumero
        print(f'{primeiroNumero} + {segundoNumero} = {soma}')
        sleep(3)
        system('cls')
        print('=== ESCOLHA UMA DAS OPÇÕES ===')
        print('[1] - Somar. \n[2] - Multiplicar. \n[3] - Maior \n[4] - Novos números. \n[0] - Sair.')
        opcao = int(input('Digite a sua opção: '))
    if opcao == 2: # Multiplicar os valores.
        multiplicacao = primeiroNumero * segundoNumero
        print(f'{primeiroNumero} x {segundoNumero} = {multiplicacao}')
        sleep(3)
        system('cls')
        print('=== ESCOLHA UMA DAS OPÇÕES ===')
        print('[1] - Somar. \n[2] - Multiplicar. \n[3] - Maior \n[4] - Novos números. \n[0] - Sair.')
        opcao = int(input('Digite a sua opção: '))
    if opcao == 3: # Verificar quem é maior.
        if primeiroNumero > segundoNumero:
            print(f'{primeiroNumero} é maior que {segundoNumero}.')
        elif primeiroNumero < segundoNumero:
            print(f'{primeiroNumero} é menor que {segundoNumero}.')
        else:
            print('Os valores são iguais!')
        sleep(3)
        system('cls')
        print('=== ESCOLHA UMA DAS OPÇÕES ===')
        print('[1] - Somar. \n[2] - Multiplicar. \n[3] - Maior \n[4] - Novos números. \n[0] - Sair.')
        opcao = int(input('Digite a sua opção: '))
    if opcao == 4: # Inserir novos números.
        primeiroNumero = int(input('Digite o primeiro número: '))
        segundoNumero = int(input('Digite o segundo número: '))
        opcao = int(input('Digite a sua opção: '))
