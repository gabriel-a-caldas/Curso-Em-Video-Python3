# Faça um programa que leia um ano qualquer
# e mostre se ele é BISSEXTO

ano = int(input('Informe o ano: '))

if (ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0):
    print('Ano é bissexto!')
else:
    print('Ano não é bissexto.')