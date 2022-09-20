# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

from cmath import sqrt

numero = int(input("Insira um número: "))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = sqrt(numero)

print(f'O dobro do numero inserido é: {dobro}')
print(f'O triplo do valor inserido é: {triplo}')
print(f'A raiz quadrada do valor inserido é: {raizQuadrada}')