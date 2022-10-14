"""
Crie um programa que leia vários números inteiros. O programa só vai parar
quando o usuário digitir o valor 999, quie é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre elas.
(desconsiderando o flag).
"""
resposta = int(input('Insira um número: '))
somatoria = 0
contador = 0

while resposta != 999:
    somatoria += resposta
    resposta = int(input('Insira um número: '))
    contador += 1
print(f'A somatória dos {contador} números digitados é: {somatoria}.')