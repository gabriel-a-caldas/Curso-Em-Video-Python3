"""
Melhore o DESAFIO 060, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar
0 termos.
"""
from os import system
from time import sleep


print('==== CALCULADORA DE PROGRESSÃO ARITIMÉTICA ====')

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão da P.A: '))
termo = primeiroTermo
contador = 1

while contador <= 10:
    print(termo, end=' ')
    termo = termo + razao
    contador += 1
resposta = int(input('\nQuantos termos você deseja mostrar? [0 para sair]. '))
while resposta != 0:
    for i in range(0, resposta):
        print(termo, end=' ')
        termo = termo + razao
    resposta = int(input('\nQuantos termos você deseja mostrar? [0 para sair]. '))
