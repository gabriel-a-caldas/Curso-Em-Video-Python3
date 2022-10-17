"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:

[A] - Quantas pessoas tem mais de 18 anos.
[B] - Quantos homens foram cadastrados.
[C] - Quantas mulheres tem menos de 20 anos.

"""
contadorHomens = contadorIdadeMulheres = contadorMaioridade = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    escolha = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    if idade >= 18:
        contadorMaioridade +=1
    if escolha == 'S':
        if sexo == 'M':
            contadorHomens += 1
        if sexo == 'F':
            if idade < 20:
                contadorIdadeMulheres += 1
    elif escolha == 'N':
        if sexo == 'M':
            contadorHomens += 1
        if sexo == 'F':
            if idade < 20:
                contadorIdadeMulheres += 1
        break
print(f'Total de pessoas com mais de 18 anos: {contadorMaioridade}.\nAo todo temos {contadorHomens} homens cadastrados.\nE temos {contadorIdadeMulheres} mulheres com menos de 20 anos.')