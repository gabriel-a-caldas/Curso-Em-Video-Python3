# Escreva um programa que faça o computador "pensar" em um inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint, random, randrange

numeroAleatorio = randint(0,5)

numero = int(input('Insira um número: '))
if numero > 6:
    numero = int(input('Este número não vale! Insira um número entre 0 e 5: '))
if numero == numeroAleatorio:
    print('Você acertou!')
else:
    print(f'Você errou, era: {numeroAleatorio}.')
