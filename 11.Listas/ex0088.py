"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista compsosta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from os import system

cadastroAlunos = []
cadastroNotas = []
totalAlunos = []
media = 0

while True:

    nome = str(input('Nome: ')).strip()
    notaUm = int(input('Nota 1: '))
    notaDois = int(input('Nota 2: '))

    cadastroAlunos.append(nome)
    cadastroNotas.append(notaUm)
    cadastroNotas.append(notaDois)
    cadastroAlunos.append(cadastroNotas[:])
    
    totalAlunos.append(cadastroAlunos[:])

    cadastroAlunos.clear()
    cadastroNotas.clear()

    resposta = str(input('Quer continuar? [S/N] ')).strip()

    if resposta in 'Nn':
        break

system('cls')



