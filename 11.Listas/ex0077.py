"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.
"""

from os import system

listaAleatoria = list()

maior = menor = 0

for numero in range(0,5):
    numeroDaLista = int(input(f'Insira o {numero+1}º valor: '))
    listaAleatoria.append(numeroDaLista)

for pos, item  in enumerate(listaAleatoria):
    if pos == 0:
        maior = menor = item
    else:
        if maior < item:
            maior = item
        if menor > item:
            menor = item

system('cls')

print(f'Na lista: {listaAleatoria}...')

print(f'O maior valor digitado foi: {maior}, nas posições: ',end=' ')

for posicao, valor in enumerate(listaAleatoria):
    if valor == maior:
        print(f'{posicao}...',end=' ')

print(f'\nO menor valor digitado foi: {menor}, nas posições: ',end=' ')

for posicao, valor in enumerate(listaAleatoria):
    if valor == menor:
        print(f'{posicao}...',end=' ')
