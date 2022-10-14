"""
Faça um programa que mostre a tabuada de vários números, um
para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
"""
from os import system

system('cls')
print('=-=-=-=-'*3)
print('CALCULANDO TABUADAS')
print('=-=-=-=-'*3)

while True:
    valor = int(input('Digite um número: '))
    print('\n')
    if valor < 0:
        break
    else:
        print(f'TABUADA DO {valor}')
        for i in range(0, 11):
            print(f'{valor} x {i} = {valor*i}')
        print('\n')
