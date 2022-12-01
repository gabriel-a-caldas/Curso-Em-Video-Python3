"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.
"""

from os import system
from time import sleep

listaAleatoria = list()

while True:
    elementoDaLista = int(input('Digite um número: '))

    if elementoDaLista not in listaAleatoria:
        listaAleatoria.append(elementoDaLista)
        print('Computando valor...')
        
        sleep(2)
        system('cls')

        print('Valor computador.')
    else:
        print('Numero duplicado! Não vou adicionar...')
        
        sleep(3)
        system('cls')

    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(listaAleatoria)