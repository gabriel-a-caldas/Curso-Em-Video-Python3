"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
arquivo simples.

O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from os import system
from imprimeElementos import imprimeMenu
from cadastro import consultaPessoas, cadastraPessoas
from limpaDados import apagaDados
from time import sleep

# Programa principal

system('cls')


while True:
    imprimeMenu('MENU PRINCIPAL')
    opcao = int(input('Sua opção: '))
    if opcao <= 0 or opcao >= 5:
        print('ERRO: Opção válida!')
    elif opcao == 1:
        consultaPessoas()
    elif opcao == 2:
        nome = str(input('Nome: '))
        try:
            idade = int(input('Idade: '))
        except (ValueError, TypeError):
            print('ERRO: Por favor, insira um inteiro válido!')
        cadastraPessoas(nome,idade)
    elif opcao == 3:
        apagaDados()
    elif opcao == 4:
        break
