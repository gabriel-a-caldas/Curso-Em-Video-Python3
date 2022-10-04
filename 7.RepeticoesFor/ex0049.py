# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# for ímpar, desconsidere-o.

from os import system

system('cls')

somaPar = 0

for i in range(0,6):
    numero = int(input('Insira um número: '))
    if numero % 2 == 0:
        somaPar += numero
print(f'A soma dos números pares é: {somaPar}')