"""

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""
from os import system

cadastroJogador = {}
golsMarcados = []
totalGols = 0
contadorTotal = 1

system('cls')

cadastroJogador['nome'] = str(input('Nome do jogador: '))
numeroPartidas = int((input(f'Quantas partidas {cadastroJogador["nome"]} jogou? ')))

for contadorPartidas in range(1,numeroPartidas+1):
    gol = int(input(f' Quantos gols na partida {contadorPartidas}? '))
    golsMarcados.append(gol)

for posicao, valores in enumerate(golsMarcados):
    totalGols += valores

cadastroJogador['gols'] = golsMarcados
cadastroJogador['total'] = totalGols

print('=-'*30)
print(cadastroJogador)
print('=-'*30)
print(f'O jogador {cadastroJogador["nome"]} jogou {numeroPartidas}.')

for gols in golsMarcados:
    print(f'  => Na partida {contadorTotal}, fez {gols}')
    contadorTotal += 1
print(f'Foi um total de {totalGols} gols.')
