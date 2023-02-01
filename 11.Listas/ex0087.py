"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista copmposta.
"""

from random import randint
from os import system
from time import sleep

jogosMegaSena = []
jogoUnicoSorteado = []

system('cls')

print('-'*30)
print('      JOGA NA MEGA SENA      ')
print('-'*30)

numeroDeJogos = int(input('Quantos jogos você quer que eu sorteie? '))

for vezesParaSortear in range(0,numeroDeJogos):
    for numeros in range(0,6):
        jogoUnicoSorteado.append(randint(1,60))
    jogosMegaSena.append(jogoUnicoSorteado[:])
    jogoUnicoSorteado.clear()

print('-=-=-=',end='')
print(F' SORTEANDO {numeroDeJogos} JOGOS ',end='')
print('-=-=-=')

for jogos in range(0,numeroDeJogos):
    print(f'Jogo {jogos+1}: {jogosMegaSena[jogos]}')
    sleep(0.8)
print('-=-='*3,end='')
print('  < BOA SORTE >  ',end='')
print('-=-='*3)
