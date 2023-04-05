"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
arquivo simples.

O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from lib.interface import *
from lib.backend import *
from time import sleep
from os import system

while True:
    resposta = menu(['Consultar pessoas cadastradas','Cadastrar uma nova pessoa','Limpar a tela','Sair do sistema'])
    if resposta == 1:
        exibePessoasCadastradas()
    elif resposta == 2:
        cadastraPessoas()
    elif resposta == 3:
        print('Limpando a tela...')
        sleep(2)
        system('cls')
    elif resposta == 4:
        cabecalho('Saindo do sistema!')
        break
    else:
        sleep(1)
        print('ERRO: Digite uma opção válida!')
