# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0, com
# uma pausa de 1 segundo entre elas.
from os import system
from time import sleep

system('cls')

print('COMEÇANDO A CONTAGEM AGORA!')
print('...')
sleep(3)
for contador in range(10,0,-1):
    print(contador)
    sleep(1)
print(' *:・ﾟ✧ '*5)
