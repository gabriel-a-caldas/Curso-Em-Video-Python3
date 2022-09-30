# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão.

from re import A


escolha = int(input('Informe qual conversão deseja fazer: \n 1 - para binário. \n 2 - para octal. \n 3 - para hexadecimal. \n Escolha: '))

if escolha == 1:
    numero = int(input('Qual número deseja converter? '))
    binario = bin(numero)
    print(f'{numero} em binário é: {binario}.')
elif escolha == 2:
    numero = int(input('Qual número deseja converter? '))
    octal = oct(numero)
    print(f'{numero} em base octal é: {octal}.')
elif escolha == 3:
    numero = int(input('Qual número deseja converter? '))
    hexadecimal = hex(numero)
    print(f'{numero} em base hexadecimal é: {hexadecimal}.')
