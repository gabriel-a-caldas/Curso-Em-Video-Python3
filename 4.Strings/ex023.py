# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome 'SANTO'

nomeCidade = str(input('Digite o nome de uma cidade: ')).upper().strip()

print(nomeCidade[:5] == 'SANTO')

