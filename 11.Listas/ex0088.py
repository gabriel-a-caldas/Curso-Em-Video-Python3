"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista compsosta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from os import system

cadastroAlunos = []
cadastroNotas = []
totalAlunos = []
mediaDosAlunos = []
media = 0

while True:

    nome = str(input('Nome: ')).strip()
    notaUm = float(input('Nota 1: '))
    notaDois = float(input('Nota 2: '))

    cadastroAlunos.append(nome)
    cadastroNotas.append(notaUm)
    cadastroNotas.append(notaDois)
    cadastroAlunos.append(cadastroNotas[:])
    
    totalAlunos.append(cadastroAlunos[:])

    cadastroAlunos.clear()
    cadastroNotas.clear()
    
    media = (notaUm + notaDois)/2

    mediaDosAlunos.append(media)

    resposta = str(input('Quer continuar? [S/N] ')).strip()

    if resposta in 'Nn':
        break

system('cls')

print('-=-='*15)
print('Nº   NOME         MEDIA')
print('-'*20)

for alunos in totalAlunos:
    posicao = totalAlunos.index(alunos)
    print(f'{posicao}     {alunos[0]}         {mediaDosAlunos[posicao]}')

