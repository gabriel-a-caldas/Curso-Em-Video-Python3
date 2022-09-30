# Crie um programa que faça o computador jogar Jokenpô com você.

from os import system
from time import sleep
from random import choice

system('cls')
print('Olá eu sou o COMPUTADOR JOKENPÔ 2000!')
sleep(2)
print('Hoje irei ganhar de você...hehehe! ᕙ(^▿^-ᕙ)')
sleep(4)
system('cls')

escolha = str(input('Faça a sua escolha! Pedra, Papel, Tesoura: ')).upper().strip()

listaOpcoesSistema = ['PEDRA', 'PAPEL', 'TESOURA']

escolhaDoSistema = choice(listaOpcoesSistema)

if escolhaDoSistema == 'PEDRA' and escolha == 'PAPEL' or escolhaDoSistema == 'PAPEL' and escolha == 'TESOURA' or escolhaDoSistema == 'TESOURA' and escolha == 'PEDRA':
    print(f'Ah não...Você ganhou! \nEU: {escolhaDoSistema} x \nVocê: {escolha} \nO vencedor é: {escolha}') # VITORIA DO JOGADOR
elif escolhaDoSistema == 'PAPEL' and escolha == 'PEDRA' or escolhaDoSistema == 'PEDRA' and escolha == 'TESOURA' or escolhaDoSistema == 'TESOURA' and escolha == 'PAPEL':
    print(f'GANHEI (¬‿¬)! \nUm mero humano não pode superar uma máquina! \nEU: {escolhaDoSistema} x \nVocê{escolha} \n O vencedor é: {escolhaDoSistema}') # VITORIA DO SISTEMA
elif escolhaDoSistema == 'PEDRA' and escolha == 'PEDRA' or escolhaDoSistema == 'PAPEL' and escolha == 'PAPEL' or escolhaDoSistema == 'TESOURA' and escolha == 'TESOURA':
    print(f'Vamos refazer... \nEU: {escolhaDoSistema} x \nVocê: {escolha} é emapte!') # EMPATE