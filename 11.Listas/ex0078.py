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
        
        sleep(1)
        system('cls')

        print('Valor computador.')
    else:
        print('Valor duplicado! Não vou adicionar...')
        
        sleep(1)
        system('cls')
        
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
listaAleatoria.sort() # Organia a lista em ordem crescente.
print(f'A lista digitada foi: {listaAleatoria}.')