"""

Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade().

Faça também um programa que importe esse módulo e use algumas dessa funções.

"""
import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {round(moeda.aumentar(preco,10),2)}')
print(f'Diminuindo 13%, temos {round(moeda.diminuir(preco,13),2)}')
