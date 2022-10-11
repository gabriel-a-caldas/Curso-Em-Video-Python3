"""
Refaça o DESAFIO 050, lendo o primeiro termo e razão de uma PA, mostrando
os 10 primeiros termos de uma progressão usando a estrutura while.
"""

print('==== CALCULADORA DE PROGRESSÃO ARITIMÉTICA ====')

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão da P.A: '))

contador = 1
progressao = 0

while contador <= 10:
    progressao = primeiroTermo + (contador-1)*razao
    print(progressao, end=' ')
    contador += 1
