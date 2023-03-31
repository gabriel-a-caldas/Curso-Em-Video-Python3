"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.
"""
def leiaInt(mensagem):
    valorInteiro = str(input(mensagem)).strip()
    valido = False

    while not valido:
        if valorInteiro.isnumeric():
            valido == True
            return valorInteiro
        else:
            print('Este valor digitado não é válido!')
            valorInteiro = str(input(mensagem)).strip()



# Programa principal
from os import system

system('cls')
numeroInteiro = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {numeroInteiro}')
