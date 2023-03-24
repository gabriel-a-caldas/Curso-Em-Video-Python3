"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""
def ficha(jogador='<desconhecido>',gols='0'):
    """
    Exibe o nome e número de gols de um jogador.
    :param jogador: (opcional) [string] nome do jodaor.
    :param gols: (opcional) [inteiro] n° de gols.
    :return retorna o nome e o número de gols:
    """
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


# Programa principal
from os import system

system('cls')

nomeEstaVazio = False
golEstaVazio = False

nome = str(input('Nome do Jogador: ')).strip()
numeroGols = str(input('Número de Gols: '))

if len(nome) == 0:
    nomeEstaVazio = True
if len(numeroGols) == 0:
    golEstaVazio = True

if nomeEstaVazio and golEstaVazio:
    print(ficha())
elif nomeEstaVazio:
    print(ficha(gols=numeroGols))
elif golEstaVazio:
    print(ficha(jogador=nome))
else:
    print(ficha(nome,numeroGols))
