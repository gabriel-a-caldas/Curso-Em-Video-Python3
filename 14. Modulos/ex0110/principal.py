"""
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre
no tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
import moeda
from os import system

system('cls')

preco = float(input('Digite o preço: R$'))
valorParaAumentar = int(input(f'Informe quanto se deve aumentar de {moeda.floatToCurrency(preco)}: '))
valorParaDiminuir = int(input(f'Informe quanto se deve diminuir de {moeda.floatToCurrency(preco)}: '))

moeda.resumo(preco,valorParaAumentar,valorParaDiminuir)
