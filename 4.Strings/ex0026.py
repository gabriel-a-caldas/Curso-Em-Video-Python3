# Faça um programa que leia o nome completo de uma pessoa,
# Mostrando em seguida o primeiro e o último nome
# separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Insira o nome completo: ')).strip()

nomeSeparado = nome.split()

primeiroNome = nomeSeparado[0]
ultimoNome = nomeSeparado[-1]

print(f'Primeiro = {primeiroNome}')
print(f'Último = {ultimoNome}')