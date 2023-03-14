"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
em um dicionário, se por acaso a CTPS for diferente de ZERO (0), o dicionário também
receberá o ano de contratação e o salário. Calcule e acrescente, além da idade, com
quantos anos a pessoa vai se aposentar.

"""
from datetime import datetime
from os import system
from time import sleep

cadastro = dict()
anoAtual = datetime.now().year

cadastro['nome'] = str(input('Nome: ')).strip()
cadastro['anoNascimento'] = int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
cadastro['idade'] = anoAtual - cadastro['anoNascimento'] 

if cadastro['CTPS'] != 0:
    cadastro['anoContratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = int(input('Salário: '))
    cadastro['aposentadoria'] =  (anoAtual - cadastro['anoContratacao']) + cadastro['idade'] + 35 

    system('cls')
    print(cadastro)
    for keys, values in cadastro.items():
        print(f'- {keys} tem o valor {values}')
        sleep(0.7)

else:
    system('cls')
    print(cadastro)
    for keys, values in cadastro.items():
        print(f'- {keys} tem o valor {values}')
        sleep(0.7)