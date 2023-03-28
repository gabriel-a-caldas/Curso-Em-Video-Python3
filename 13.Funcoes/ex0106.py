"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manula vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""
from os import system
from time import sleep


def cabecalho(mensagem):
    tamanhoCabecalho = len(mensagem) + 4

    print('~' * tamanhoCabecalho)
    print(f' {mensagem} ')
    print('~' * tamanhoCabecalho)


def manualPython(resposta):
    """
    Sistema de ajuda PyHELP, digite uma Função ou biblioteca e obtenha o manual de uso dele.
    :param comando: Função ou biblioteca a ser procurado.
    """
    cabecalho(f'Acessando o manual do {resposta}...')
    sleep(1)
    help(resposta)
    sleep(2)


# Programa principal

resposta = ''

while True:

    cabecalho('SISTEMA DE AJUDA PyHELP')
    
    resposta = str(input('Função ou biblioteca > '))

    if resposta.upper() == 'FIM':
        break
    else:
        manualPython(resposta)

sleep(1)
cabecalho('ATÉ LOGO!')
sleep(2)
system('cls')
