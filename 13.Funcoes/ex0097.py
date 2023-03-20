"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realiza a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada.
"""
from time import sleep
from os import system

system('cls')

def contador(inicio, fim, passo):

    print('-=' * 30)
    if passo == 0:
        passo = 1
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        sleep(1)
        for contagem in range(inicio, fim, passo):
            print(contagem,end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        passo = abs(passo)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        sleep(1)
        for contagem in range(inicio, fim, -passo):
            print(contagem,end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


# Programa principal
contador(1,10,1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
