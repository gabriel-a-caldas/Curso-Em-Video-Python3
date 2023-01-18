"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

"""
listaAleatoria = list()
contador = contadorCinco = 0


while True:

    numeroLista = int(input('Insira um número: '))
    listaAleatoria.append(numeroLista)
    contador += 1

    if numeroLista == 5:
        contadorCinco += 1

    resposta = str(input('Deseja continuar? [S/N] ')).strip()

    listaAleatoria.sort(reverse=True) # Organiza a lista de maneira decrescente.

    if resposta in 'Nn':
        break

print(f'Foram digitados: {contador} números.')

print(f'A lista organizada de forma decrescente é: {listaAleatoria}')

if contadorCinco > 0: 
    print(f'O valor 5 foi digitado: {contadorCinco} vezes.')
else:
    print(f'O valor 5 não foi digitado nenhuma vez.')
