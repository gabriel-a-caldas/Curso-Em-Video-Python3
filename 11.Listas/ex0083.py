"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

"""

cadastroPessoas = list()
totalPessoas = list()
pessoasMaisLeves = list()
pessoasMaisPesadas = list()

resposta = 'Ss'
contadorTotalPessoas = contadorMaisPesadas = contadorMenosPesadas = 0
maior = menor = 0


while True:
    
    cadastroPessoas.append(str(input('Nome: ')).strip())
    cadastroPessoas.append(str(input('Peso: ')).strip())
    contadorTotalPessoas += 1
    totalPessoas.append(cadastroPessoas[:])
    cadastroPessoas.clear()

    resposta = str(input('Deseja continuar? [S/N] '))
    
    if resposta in 'Nn':
        break

for posicao, pessoas in enumerate(totalPessoas):
    if posicao == 0:
        maior = menor = 0
    if totalPessoas[posicao][1] > totalPessoas[posicao][1]:
        maior = totalPessoas[posicao][1]
        contadorMaisPesadas += 1
    elif totalPessoas[posicao][1] < totalPessoas[posicao][1]:
        menor = totalPessoas[posicao][1]
        contadorMenosPesadas += 1

print(f'Foram cadastradas: {contadorTotalPessoas} pessoas em nosso sistema.')
