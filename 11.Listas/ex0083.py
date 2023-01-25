"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

"""
cadastroPessoas = list()
totalPessoas = list()
maiorPeso = menorPeso = 0

while True:

    cadastroPessoas.append(str(input('Nome: ')).strip())
    cadastroPessoas.append(int(input('Peso: ')))

    totalPessoas.append(cadastroPessoas[:])

    if len(totalPessoas) == 1:
        maior = menor = cadastroPessoas[1]
    else:
        if maior < cadastroPessoas[1]:
            maior = cadastroPessoas[1]
        if menor > cadastroPessoas[1]:
            menor = cadastroPessoas[1]

    cadastroPessoas.clear()

    resposta = str(input('Deseja continuar? [S/N] '))

    if resposta in 'Nn':
        break
    
print(f'Ao todo, você cadsatrou: {len(totalPessoas)} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de: ',end='')
for pessoas in totalPessoas:
    if maior == pessoas[1]:
        print(f'[{pessoas[0]}]',end=' ')
print(f'\nO menor peso foi de {menor} kg. Peso de: ',end='')
for pessoas in totalPessoas:
    if menor == pessoas[1]:
        print(f'[{pessoas[0]}]',end=' ')
