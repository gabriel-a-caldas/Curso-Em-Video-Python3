# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt, pow, hypot


catetoOposto = float(input('Digite o valor do catetoto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f'O valor da hipotenusa do triângulos de lados {catetoOposto} e {catetoAdjacente} é: {hipotenusa}.')