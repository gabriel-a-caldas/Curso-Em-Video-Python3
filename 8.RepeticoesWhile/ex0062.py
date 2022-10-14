"""
Escreva um programa que leia um numero n inteiro qualquer
e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci
"""
escolha = int(input('Informe quantos termos a sequência terá: '))

somaFibonacci = 0
termoAnterior = 1
termoPosterior = 0

for i in range(0,escolha):
        somaFibonacci = termoAnterior + termoPosterior
        termoAnterior = termoPosterior
        termoPosterior = somaFibonacci
        print(somaFibonacci,end=' ')
print('FIM')