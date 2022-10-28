"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.
"""
lista = list(int(input('Insira um número: '))for c in range(0,5))

maior = menor = 0
print('A lista: ',end='')
for pos, item in enumerate(lista):
    if pos == 0:
        maior = item
        menor = item
    else:
        if maior < item:
            maior = item
        if menor > item:
            menor = item
    print(f'{pos}',end=' ')
print(f'\nO maior valor digitado foi {maior} e o menor {menor}.')
