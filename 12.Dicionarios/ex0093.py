"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No Final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) UIma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média. 
"""
from os import system
from time import sleep

cadastroPessoas = {}
totalPessoas = []
mulheres = []
pessoasAcimaDaMediaIdade = []
mediaIdade = somatorioIdade = contadorPessoasCadastradas = 0

system('cls')

while True:

    cadastroPessoas['nome'] = str(input('Nome: ')).strip()
    cadastroPessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    
    if cadastroPessoas['sexo'] == 'F':
        mulheres.append(cadastroPessoas['nome'])

    cadastroPessoas['idade'] = int(input('Idade: '))
    contadorPessoasCadastradas += 1
    
    totalPessoas.append(cadastroPessoas.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip()

    if resposta in 'Nn':
        break

for posicao, pessoas in enumerate(totalPessoas):
    somatorioIdade += totalPessoas[posicao]['idade']
mediaIdade = somatorioIdade/contadorPessoasCadastradas

print('=-'*30)
print(f'- O grupo tem {contadorPessoasCadastradas} pessoas.')
print(f'- A média de idade é de {round(mediaIdade,2)}')
print('- As mulheres cadastradas foram: ',end='')
for mulheresCadastradas in mulheres:
    print(mulheresCadastradas,end=' ')
    sleep(0.7)
print()
print('- Lista das pessoas que estão acima da média de idade: ')
print()
for posicaoDois, pessoasDois in enumerate(totalPessoas):
    if totalPessoas[posicaoDois]['idade'] > mediaIdade:
        print(f'nome = {totalPessoas[posicaoDois]["nome"]}; sexo = {totalPessoas[posicaoDois]["sexo"]}; idade = {totalPessoas[posicaoDois]["idade"]};')
        print()
        sleep(0.7)
print('<< ENCERRADO >>')
