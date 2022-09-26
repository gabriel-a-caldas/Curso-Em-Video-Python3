# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "SILVA" no nome

nomeCompleto = str(input('Informe o nome completo: ')).upper()

achaStringSilva = nomeCompleto.find('SILVA')

if achaStringSilva != -1:
    print('O seu nome possui Silva!')
else:
    print('O seu nome não possui Silva!')