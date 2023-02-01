"""
Crie um programa onde o usuárioo possa digitar sete valores numéricos
e cadsatre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
totalNumeros = [[],[]]

for indice in range(1,8):

    numeroUsuario = int(input(f'Digite o {indice}º valor: '))

    if numeroUsuario % 2 == 0:
        totalNumeros[0].append(numeroUsuario)
    else:
        totalNumeros[1].append(numeroUsuario)

totalNumeros[0].sort()
totalNumeros[1].sort()

print(f'Os valores pares digitados foram: {totalNumeros[0]}')
print(f'Os valores ímpares digitados foram: {totalNumeros[1]}')


    