"""

Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes de aproveitamento de cada jogador.

"""
from os import system

cadastroJogador = {}
golsMarcados = []
totalJogadores = []
totalGols = 0
contadorTotal = 0

system('cls')

while True:

    cadastroJogador['nome'] = str(input('Nome do jogador: '))
    numeroPartidas = int((input(f'Quantas partidas {cadastroJogador["nome"]} jogou? ')))

    for contadorPartidas in range(0,numeroPartidas):
        gol = int(input(f' Quantos gols na partida {contadorPartidas}? '))
        golsMarcados.append(gol)
    
    for gols in golsMarcados:
        totalGols += gols

    cadastroJogador['gols'] = golsMarcados[:]
    cadastroJogador['total'] = totalGols

    totalJogadores.append(cadastroJogador.copy())

    golsMarcados.clear()
    totalGols = 0

    resposta = str(input('Deseja continuar? [S/N] '))
    print('-'*40)

    if resposta in 'Nn':
        break

system('cls')

print(f'cod \tnome \tgols \ttotal')
print('-'*30)
for posicao, jogadores in enumerate(totalJogadores):
    print(f'{posicao:<} \t{totalJogadores[posicao]["nome"]} \t{totalJogadores[posicao]["gols"]} \t{totalJogadores[posicao]["total"]}')
print('-'*30)

while True:

    resposta = int(input('Mostrar dados de qual jogador? [999 para] '))
    if resposta == 999:
        break
    elif 0 <= resposta <= len(totalJogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {totalJogadores[resposta]["nome"]}')
        for posicao, gols in enumerate(totalJogadores[resposta]["gols"]):
            print(f'\t No jogo {posicao} fez {gols} gols.')
    else:
        print(f'ERRO! Não existe jogador com o código {resposta}')
