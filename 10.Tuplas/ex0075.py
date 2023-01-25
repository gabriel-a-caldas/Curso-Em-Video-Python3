"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência.

No final mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('Lapis', 0.99,
            'Borracha', 2,
            'Caderno', 20,
            'Estojo', 12,
            'Mochila', 150,
            'Compasso', 7.99,
            'Caneta', 1.99,
            'Corretivo', 3.99,
            'Lapiseira', 5.99
            )
print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}',end='')
    else:
        print(f'R$ {listagem[posicao]:>7.2f}')
