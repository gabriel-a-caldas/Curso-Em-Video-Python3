"""

Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.

"""

cadastroAluno = {}

cadastroAluno['Nome'] = str(input('Nome: ')).strip()
cadastroAluno['Media'] = int(input(f'Média de {cadastroAluno["Nome"]}: '))

for key, values in cadastroAluno.items():
    print(f'{key} é igual a {values}')
if cadastroAluno['Media'] >= 7:
    print('Situação é igual a Aprovado.')
else:
    print('Situação é igual a Reprovado.')