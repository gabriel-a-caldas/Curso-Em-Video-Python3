"""
Melhore o jogo do DESAFIO 028 em que o computador vai "pensar" em um
númnero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

numeroAleatorio = randint(0,10)
contador = 1

palpite = int(input('Insira o seu palpite: '))

while palpite != numeroAleatorio:
    if palpite > 10:
        palpite = int(input('Este número não vale! Insira um número entre 0 e 10: '))
    if palpite != numeroAleatorio:
        palpite = int(input('Você errou! \nInsira seu palpite novamente: '))
        contador += 1
    elif palpite == numeroAleatorio:
        print('Parabéns! Você acertou!')
        contador += 1
print(f'Foram necessárias: {contador} tentativas para acertar o número: {numeroAleatorio}')
