# Crie um programa que leia um número inteiro e mostre na tela
# se ele é PAR ou ÍMPAR

numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é ímpar')