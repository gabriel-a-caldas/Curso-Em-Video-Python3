"""
Crie um programa em que o usuário possa digitar cinco valores numéricos e
cadastr-os em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenda na tela.
"""
from time import sleep

aux = 0

listaOrdenada = list()

for contador in range(0,5):

    numeroLista = int(input('Insira um número: '))

    if contador == 0 or numeroLista > listaOrdenada[-1]:
        listaOrdenada.append(numeroLista)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(listaOrdenada):
            if numeroLista <= listaOrdenada[posicao]:
                listaOrdenada.insert(posicao, numeroLista)
                print(f'Adicionado na posição: {posicao}')
                break
            posicao += 1
print(f'Os valores adicionados na lista foram: {listaOrdenada}')
        
