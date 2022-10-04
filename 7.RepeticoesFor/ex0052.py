# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

print('======== VERIFICADOR DE PALÍNDROMO ========')

frase = str(input('Informe uma frase: ')).strip()

fraseSemEspacos = frase.replace(' ','')
tamanhoFrase = len(fraseSemEspacos)

for i in frase:
    print(i)

