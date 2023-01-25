"""
Crie um programa que leia vários números inteiros. O programa
só irá parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final mostre quantos números foram
digitados e qual foi a soma entre eles. (Desconsiderando o flag)
"""

soma = contador = 0

while True:
    numero = int(input('Insira um número: '))
    if numero == 999:
        break
    else:
        soma += numero
    contador += 1
print(f'A soma dos {contador} números é: {soma}.')
