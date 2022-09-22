# Um professor quer sortear um dos seus quatro anos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# escolhido.

import random

nome1 = input('Informe o nome do 1º aluno: ')
nome2 = input('Informe o nome do 2º aluno: ')
nome3 = input('Informe o nome do 3º aluno: ')
nome4 = input('Informe o nome do 4º aluno: ')
lista = [nome1, nome2, nome3, nome4]

nomeSorteado = random.choice(lista)

print(f'O nome escolhido foi a limpar o quadro foi: {nomeSorteado}')