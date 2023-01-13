"""
Crie um programa em que o usuário possa digitar cinco valores numéricos e
cadastr-os em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenda na tela.
"""

listaOrdenada = list()

while True:
    listaOrdenada.append(int(input('Digite um valor: ')))
    for posicao, elementoDaLista in enumerate(listaOrdenada):
        if posicao == 0:
            print('Adicionado ao final da lista...')
        else:
            if listaOrdenada[posicao] > listaOrdenada[posicao+1]: #Verifica se o valor é maior.
                listaOrdenada[posicao]
    if len(listaOrdenada) == 5:
        break