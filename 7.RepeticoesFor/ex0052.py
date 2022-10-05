# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

print('======== VERIFICADOR DE PALÍNDROMO ========')

frase = str(input('Informe uma frase: ')).strip().upper()

fraseSemEspacos = frase.replace(' ','')
tamanhoFrase = len(fraseSemEspacos)

inverso = ''

for letra in range(tamanhoFrase -1, -1, -1):
    inverso += fraseSemEspacos[letra]
if inverso == fraseSemEspacos:
    print('É um palíndromo!')
else:
    print('Não é palíndromo!')