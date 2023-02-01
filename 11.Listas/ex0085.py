"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado.
    [][][]
    [][][]
    [][][]
No final, mostre a matriz na tela, com a formatação correta.
"""

from os import system

matriz = [[], [], []]
cadastroValores = []

for linhas in range(1,4):

    for colunas in range(1,4):

        valor = int(input(f'Digite o valor da {linhas}ª linha x {colunas}ª coluna da matriz: '))
        
        if linhas == 1:
            cadastroValores.append(valor)
            matriz[0].append(cadastroValores[:])
        elif linhas == 2:
            cadastroValores.append(valor)
            matriz[1].append(cadastroValores[:])
        elif linhas == 3:
            cadastroValores.append(valor)
            matriz[2].append(cadastroValores[:])
        cadastroValores.clear()

system('cls')

print('Sua matriz: ')

for linhas in range(0,3):
    for colunas in range(0,3):
        print(f'{matriz[linhas][colunas]}',end='')
    print()
