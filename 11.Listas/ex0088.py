"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista compsosta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
"""
from os import system
from time import sleep

system('cls')

cadastroAlunos = []
cadastroNotas = []
totalAlunos = []
totalNotas = []
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
    totalNotas.append(cadastroNotas[:])

    cadastroAlunos.clear()
    cadastroNotas.clear()
    
    media = (notaUm + notaDois)/2

    mediaDosAlunos.append(media)

    resposta = str(input('Quer continuar? [S/N] ')).strip()

    if resposta in 'Nn':
        break

system('cls')

print('-=-='*10)
print('Nº   NOME         MEDIA')
print('-'*40)

for alunos in totalAlunos:
    posicaoAlunos = totalAlunos.index(alunos)
    print(f'{posicaoAlunos}     {alunos[0]}     {mediaDosAlunos[posicaoAlunos]}')

escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

while escolha != 999:
    print(f'Notas de {totalAlunos[escolha][0]} são {totalNotas[escolha]}')
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

sleep(2)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')