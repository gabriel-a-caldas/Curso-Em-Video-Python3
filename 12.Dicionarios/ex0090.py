"""
Crie um programa em que 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
eses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que
o vencedor tirou o maior número no dado.
"""
from os import system
from time import sleep
from random import randint

system('cls')

resultados = {}
contador = 1

for numero in range(1,5):
    resultados[f'jogador{numero}'] = randint(1,6)

print('Valores sorteados:')
sleep(1)

for key, values in resultados.items():
    print(f'   O {key} tirou {values}')
    sleep(0.7)

print('Ranking dos jogadores:')
sleep(1)

resultadosOrdenados = dict(sorted(resultados.items(), key=lambda item:item[1], reverse=True))

for key, value in resultadosOrdenados.items():
    print(f'   {contador}º lugar: {key} com {value}')
    sleep(0.7)
    contador +=1
