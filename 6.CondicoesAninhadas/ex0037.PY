"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O Primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
"""
primeiroValor = int(input('Digite o 1º valor: '))
segundoValor = int(input('Digite o 2º valor: '))

if primeiroValor > segundoValor:
    print(f'O 1º valor, {primeiroValor} é maior que {segundoValor}.')
elif segundoValor > primeiroValor:
    print(f'O 2º valor, {segundoValor} é maior que {primeiroValor}.')
else:
    print(f'Não existe valor maior, os dois valores são iguais.')
