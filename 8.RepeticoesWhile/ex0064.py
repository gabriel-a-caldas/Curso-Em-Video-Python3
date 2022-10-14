"""
Crie um programa que leia vários números inteiros. No final da execução,
mmostre a média entre todos os valores e qual foi o maior e o menor valores
lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a 
digitar os valores.
"""

resposta = 'S'
contador = soma = media = 0
maiorNumero = menorNumero = 0

while resposta in 'Ss':
    contador += 1
    numero = int(input('Digite um número: '))
    soma += numero
    if contador == 1:
        maiorNumero = menorNumero = numero
    else:
        if numero > maiorNumero:
            maiorNumero = numero
        if numero < menorNumero:
            menorNumero = numero
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma/contador    

print(f'Foram digitados: {contador} números. A média é: {round(media,2)}.')
print(f'O maior número é: {maiorNumero} e o menor número é {menorNumero}.')