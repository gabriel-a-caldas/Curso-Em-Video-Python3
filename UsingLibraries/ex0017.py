# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import cos, degrees, sin, tan, degrees

anguloGraus = float(input('Informe o valor do ângulo em graus: '))

cossenoRadianos = cos(anguloGraus)
senoRadianos = sin(anguloGraus)
tangenteRadianos = tan(anguloGraus)

print(f'O ângulo {anguloGraus}, possui: \n Seno: {senoRadianos} \n Cosseno: {cossenoRadianos} \n Tangente: {tangenteRadianos}')