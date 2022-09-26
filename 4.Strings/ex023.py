# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome 'SANTO'

nomeCidade = str(input('Digite o nome de uma cidade: ')).upper()

listaPalavras = nomeCidade.split()

if listaPalavras[0] == 'SANTO':
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')

