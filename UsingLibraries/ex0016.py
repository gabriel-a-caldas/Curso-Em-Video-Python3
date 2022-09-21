# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt, pow


catetoOposto = float(input('Digite o valor do catetoto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt(pow(catetoOposto,2) + pow(catetoAdjacente,2))

print(f'O valor da hipotenusa do triângulos de lados {catetoOposto} e {catetoAdjacente} é: {hipotenusa}.')