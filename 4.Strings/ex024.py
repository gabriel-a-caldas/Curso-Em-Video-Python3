# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "SILVA" no nome

nomeCompleto = str(input('Informe o nome completo: ')).upper()

if 'SILVA' in nomeCompleto:
    print('O seu nome possui Silva!')
else:
    print('O seu nome não possui Silva!')