"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamdo show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela de processo de cálculo do fatorial.
"""
from os import system


def fatorial(numeroASerCalculado, show=False):
    """
    Função que calcula o fatorial de um número.
    :param numeroASerCalculado: Número a ser calculado.
    :param show: (opcional) Mostra o processo de cálculo do fatorial.
    :return: O valor do fatorial do numeroaASerCalculado
    """
    from math import factorial
    totalFatorial = 1

    if show == False:
        print('-'*50)
        return factorial(numeroASerCalculado)
    else:
        print('-'*50)
        for fatorial in range(numeroASerCalculado,0,-1):
            totalFatorial = totalFatorial * fatorial
            print(f'{fatorial}',end='')
            print(' x ' if fatorial > 1 else ' = ',end='')
        return totalFatorial


#Programa principal
system('cls')

valor = int(input('Qual número deseja calcular o fatorial? '))
mostraProcessoFatorial = str(input('Deseja mostrar o cálculo do número? [S/N] '))

if mostraProcessoFatorial in 'Ss':
    print(fatorial(valor, True))
else:
    print(fatorial(valor))
