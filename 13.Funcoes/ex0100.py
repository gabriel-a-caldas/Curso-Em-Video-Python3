"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função
anterior.
"""
from time import sleep
from os import system
from random import randint

system('cls')

def sorteia():
    lista = []
    print('Sorteando 5 valores da lista: ',end='')
    for valores in range(0,5):
        numeroAleatorio = randint(0,9)
        print(numeroAleatorio, end=' ', flush=True)
        lista.append(numeroAleatorio)
        sleep(0.5)
    print('PRONTO!')
    return lista


def somaPar(lista):
    somaPar = 0

    for valores in lista:
        if valores % 2 == 0:
            somaPar += valores
    print(f'Somando os valores pares de {lista}, temos {somaPar}')


# Programa principal
listaAleatoria = sorteia()
somaPar(listaAleatoria)
