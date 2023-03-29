"""
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
valores como um valor monetário formatado.
"""
import moeda
from os import system

system('cls')

preco = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.floatToCurrency(preco)} é {moeda.floatToCurrency(moeda.metade(preco))}')
print(f'O dobro de {moeda.floatToCurrency(preco)} é {moeda.floatToCurrency(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.floatToCurrency(moeda.aumentar(preco,10))}')
print(f'Diminuindo 13%, temos {moeda.floatToCurrency(moeda.diminuir(preco,10))}')
