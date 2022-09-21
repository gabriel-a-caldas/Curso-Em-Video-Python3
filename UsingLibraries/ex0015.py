# Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira

# OUTPUT:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
from math import trunc

numero = float(input('Digite um número: '))

parteInteira = trunc(numero)

print(f'O número {numero} tem a parte inteira {parteInteira}')