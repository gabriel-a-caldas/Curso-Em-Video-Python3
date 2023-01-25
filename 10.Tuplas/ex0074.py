"""
Desenvolva um  programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais forma os números pares.
"""

tupla = tuple(int(input('Digite um valor: ')) for i in range(1,5))

verificaValorNove = tupla.count(9)

print(f'Você digitou os valores: {tupla}')

print(f'O valor 9 apareceu {verificaValorNove} vezes.')
    
if 3 in tupla:
    print(f'O valor 3 foi digitado {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
    
print(f'Os valores pares digitados foram:',end=' ')

for i, item in enumerate(tupla):
    if item%2==0:
        print(item,end=' ')
