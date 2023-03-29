"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado vai ser ou não formatado pela função floatToCurrency(), desenvolvida
no desafio 108.
"""
import moeda
from os import system

system('cls')

preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.floatToCurrency(preco)} é {moeda.metade(preco)}')
print(f'O dobro de {moeda.floatToCurrency(preco)} é {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco,10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco,10)}')
