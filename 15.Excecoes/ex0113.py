"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitação
de um número de tipo inválido. Aproveite e crie a função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(mensagem):
    while True:
        try:
            numeroInteiro = int(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário decidiu não informar este número')
            return 0
        else:
            return numeroInteiro


def leiaFloat(mensagem):
    while True:
        try:
            numeroReal = float(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: Digite um número real válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário decidiu não informar este valor.')
        else:
            return numeroReal   


# Programa principal
from os import system

system('cls')

numero = leiaInt('Digite um valor inteiro: ')
segundoNumero = leiaFloat('Digite um real: ')
print(f'O valor digitado inteiro digitado foi {numero} e real foi {segundoNumero}')
