"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quiando o jogador PERDER,
mostrando o total das vitórias consecutivas que ele conquistou
no final do jogo.
"""
from os import system
from random import randint

system('cls')
print('=-=-=-'*4)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=-=-'*4)

soma = 0
contaVitorias = 0

while True:
    numero = int(input('Escolha o seu número: '))
    if numero > 10:
        print('Você só tem 10 dedos! Escolha um valor menor!')
        numero = int(input('Escolha o seu número: '))
    escolha = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()
    escolhaComputador = randint(0,10)
    soma = numero + escolhaComputador
    if escolha == 'P': # PAR
        if soma%2 == 0:
            print('-----'*4)
            print('VOCÊ VENCEU!') # VITÓRIA DO JOGADOR
            print(f'Você jogou {numero} e o computador {escolhaComputador}. Total de {soma} deu PAR.')
            print('-----'*4)
            contaVitorias += 1
        else:
            print('-----'*4)
            print('GAMER OVER!') # VITÓRIA DO COMPUTADOR
            print(f'Você jogou {numero} e o computador {escolhaComputador}. Total de {soma} deu ÍMPAR.')
            print('-----'*4)
            break
    elif escolha == 'I': # ÍMPAR
        if soma%2 != 0:
            print('-----'*4)
            print('VOCÊ VENCEU!') # VITÓRIA DO JOGADOR
            print(f'Você jogou {numero} e o computador {escolhaComputador}. Total de {soma} deu ÍMPAR.')
            print('-----'*4)
            contaVitorias += 1
        else:
            print('-----'*4)
            print('GAME OVER!') # VITÓRIA DO COMPUTADOR
            print(f'Você jogou {numero} e o computador {escolhaComputador}. Total de {soma} deu ÍMPAR.')
            print('-----'*4)
            break
if contaVitorias == 0:
    print('Você NÃO venceu!')
else:
    print(f'Você venceu {contaVitorias} vezes.')
