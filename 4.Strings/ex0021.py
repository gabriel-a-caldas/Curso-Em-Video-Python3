# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nomeCompleto = str(input("Informe o seu nome: "))

nomeMaiusculas = nomeCompleto.upper()
nomeMinusculas = nomeCompleto.lower()
nomeSemEspacos = nomeCompleto.replace(' ','')
nomeAoTodo = len(nomeSemEspacos)
nomeSeparado = nomeCompleto.split()

primeiroNome = nomeSeparado[0]
quantidadeLetrasPrimeiroNome = len(primeiroNome)

print(f'Seja bem-vindo, {nomeCompleto}!')
print(f'Seu nome maiúsculo: {nomeMaiusculas}')
print(f'Seu nome minúsculo: {nomeMinusculas}')
print(f'Seu nome completo tem: {nomeAoTodo} letras!')
print(f'O nome: {primeiroNome}, tem {quantidadeLetrasPrimeiroNome} letras!')