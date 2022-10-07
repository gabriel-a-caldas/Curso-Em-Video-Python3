"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.
"""

somaTotal = 0
mediaIdade = 0
maisVelho = 0
nomeDoMaisVelho = ''
contaIdadeMulher = 0

for i in range(1,5):
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo? (masc/fem) ')).strip().upper()
    
    somaTotal += idade
    mediaIdade = somaTotal/4

    if sexo == 'MASC':
        if i == 1:
            maisVelho = idade
        else:
            if idade > maisVelho:
                maisVelho = idade
                nomeDoMaisVelho = nome
    elif sexo == 'FEM':
        if idade < 20:
            contaIdadeMulher += 1

print(f'A média de idade do grupo é {mediaIdade} anos.')
print(f'O homem mais velho é o {nomeDoMaisVelho} com {maisVelho} anos.')
print(f'Existem {contaIdadeMulher} mulheres com menos de 20 anos.')