# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

anguloGraus = float(input('Informe o valor do ângulo em graus: '))

cosseno = cos(radians(anguloGraus))
seno = sin(radians(anguloGraus))
tangente = tan(radians(anguloGraus))

print(f'O ângulo {anguloGraus}, possui: \n Seno: {seno} \n Cosseno: {cosseno} \n Tangente: {tangente}')