"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.
"""
from os import system

def leiaInt(numero):

    while not numero.isnumeric():
        print('ERRO! Digite um valor válido')
        numero = str(input('Digite um número: ')).strip()
    if numero.isnumeric():
        print(f'Você acabou de digitar {numero}')


# Programa principal
system('cls')
numero = str(input('Digite um número: '))

leiaInt(numero)
