"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista compsosta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
"""
from os import system
from time import sleep

system('cls')

totalAlunos = []
media = 0

while True:

    nome = str(input('Nome: ')).strip()
    notaUm = float(input('Nota 1: '))
    notaDois = float(input('Nota 2: '))

    media = (notaUm + notaDois)/2

    totalAlunos.append([nome,[notaUm, notaDois], media])
    
    resposta = str(input('Quer continuar? [S/N] ')).strip()

    if resposta in 'Nn':
        break

system('cls')

print('-=-='*10)
print(f'{"Nº":<6}{"NOME":<10}{"MEDIA":>8}')
print('-'*40)

for alunos in totalAlunos:
    posicaoAlunos = totalAlunos.index(alunos)
    print(f'{posicaoAlunos:<6}{alunos[0]:<10}{alunos[2]:>8}')

escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

while escolha != 999:
    print(f'Notas de {totalAlunos[escolha][0]} são {totalAlunos[escolha][1]}')
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

sleep(1)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')