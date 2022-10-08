"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
correto
"""

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('ERRO! Esta informação não é válida!')
    sexo = str(input('Informe o sexo [M/F]: '))
if sexo == 'M':
    print('Seja bem-vindo!')
elif sexo == 'F':
    print('Seja bem-vinda!')