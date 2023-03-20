"""
Faã um programa que tenha uma função chamada maior(), que recebe vários
parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é maior.
"""
from time import sleep
from os import system

system('cls')

def verificaMaior(*numeros):
    maior = 0
    
    print('-='*30)
    print('Analisando os valores passados...')  

    for valores in numeros:
        print(valores,end=' ', flush=True)
        sleep(0.5)

    print(f'Foram informados {len(numeros)} ao todo.')

    for posicao, valoresTupla in enumerate(numeros):
        if posicao == 0:
            maior = valoresTupla
        if maior < valoresTupla:
            maior = valoresTupla
    
    sleep(1)

    print(f'O maior valor informado foi: {maior}.')
    
    sleep(1)


# Programa Principal
verificaMaior(2, 9, 4, 5, 7, 1)
verificaMaior(4, 7, 0)
verificaMaior(1, 2)
verificaMaior(6)
verificaMaior()