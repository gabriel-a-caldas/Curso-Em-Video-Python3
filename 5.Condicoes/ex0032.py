# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

numeroUm = float(input('Insira um número: '))
numeroDois = float(input('Insira um número: '))
numeroTres = float(input('Insira um número: '))

menor = numeroUm
# verificando quem é menor
if numeroDois < numeroUm and numeroDois < numeroTres:
    menor = numeroDois
if numeroTres < numeroUm and numeroTres < numeroDois:
    menor = numeroTres
# verificando quem é maior
maior = numeroUm
if numeroDois > numeroUm and numeroDois > numeroTres:
    maior = numeroDois
if numeroTres > numeroUm and numeroTres > numeroDois:
    maior = numeroTres
print(f'{menor} é o menor.')
print(f'{maior} é o maior.')
