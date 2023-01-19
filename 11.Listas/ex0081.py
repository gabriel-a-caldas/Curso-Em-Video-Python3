"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e
os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo gerado das três listas.
"""

listaOriginal = list()
listaPar = list()
listaImpar = list()


while True:
    
    numeroLista = int(input('Insira um número: '))
    listaOriginal.append(numeroLista)

    resposta = str(input('Deseja continuar? [S/N] ')).strip()

    if resposta in 'Nn':
        break

for posicao, itemLista in enumerate(listaOriginal): # Percorre a lista gerada procurando por números pares.
    if listaOriginal[posicao] % 2 == 0:
        listaPar.append(itemLista)
    else:
        listaImpar.append(itemLista)

print(f'Lista: {listaOriginal}')
print(f'Números pares: {listaPar}')
print(f'Números impares: {listaImpar}')
