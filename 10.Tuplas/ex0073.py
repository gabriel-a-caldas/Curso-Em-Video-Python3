"""
Crie um programa aleatório que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla
"""
from random import randrange

tuplaAleatoria = (randrange(0,1000),randrange(0,1000),randrange(0,1000),randrange(0,1000),randrange(0,1000))

print(f'Tupla: {tuplaAleatoria}.')
print(f'O maior valor foi: {max(tuplaAleatoria)}.')
print(f'O menor valor foi: {min(tuplaAleatoria)}.')