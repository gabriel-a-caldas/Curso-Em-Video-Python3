# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.
# No final, mostre os 10 primeiros termos dessa progressão.

from time import sleep

print('========= CALCULADORA DE P.A =========')

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão da P.A: '))

progressao = 0

for i in range(1, 11):
    progressao = primeiroTermo + (i-1)*razao
    print(progressao)
    sleep(1)
