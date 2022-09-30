# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
#
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

primeiroValor = int(input('Informe o primeiro valor: '))
segundoValor = int(input('Informe o segundo valor: '))

if primeiroValor > segundoValor:
    print(f'O primeiro valor é maior.')
elif segundoValor > primeiroValor:
    print(f'O segundo valor é maior.')
elif primeiroValor == segundoValor:
    print('Não existe valor maior, os dois são iguais.')
