"""
Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

quantidadeElementosTupla = int(input('Informe quantas palavras a Tupla terá: '))

tupla = tuple(str(input('Insira a palavra: ')).lower().strip()for i in range (0,quantidadeElementosTupla))

for posicao, item in enumerate(tupla):
    print(f'\nA palavra: {item.upper()} tem as vogais: ',end='')
    for letra in item:
        if letra in 'aeiou':
            print(f'{letra}',end=' ')
