"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
c) O maior valor da segunda linha.
"""
from os import system

matriz = [[0,0,0], [0,0,0], [0,0,0]]
totalValoresTerceiraColuna = totalValorePares = maiorSegundaLinha = 0


for linhas in range(0,3):

    for colunas in range(0,3):

        valorMatriz = int(input(f'Digite o valor da {linhas+1}ª linha x {colunas+1}ª coluna: '))

        matriz[linhas][colunas] = valorMatriz

        if valorMatriz % 2 == 0:
            totalValorePares += valorMatriz 

        totalValoresTerceiraColuna += matriz[linhas][2]

        if colunas == 0:
            maiorSegundaLinha = matriz[1][colunas]
        else:
            if maiorSegundaLinha < matriz[1][colunas]:
                maiorSegundaLinha = matriz[1][colunas]

print('Sua matriz: ')
for linhas in range(0,3):
    for colunas in range(0,3):
        print(f'[ {matriz[linhas][colunas]} ]',end='')
    print()

print(f'A soma dos valores pares é: {totalValorePares}')
print(f'A soma dos valores da terceira coluna é: {totalValoresTerceiraColuna}')
print(f'O maior valor da segunda linha é: {maiorSegundaLinha}')