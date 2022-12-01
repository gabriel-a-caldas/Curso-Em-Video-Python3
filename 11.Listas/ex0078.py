"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.
"""
listaAleatoria = []
resposta = 'S'

while True:
    if resposta == 'N':
        break
    if resposta == 'S':
        valorDigitado = listaAleatoria.append(int(input('Digite um número: ')))
        
        ultimoValorDaLista = listaAleatoria[len(listaAleatoria)-1]

        if valorDigitado == ultimoValorDaLista:
            print('Valor duplicado! Não vou adicionar...')
            listaAleatoria.pop()
            resposta = input('Deseja continuar? [S/N] ').strip().upper()
        resposta = input('Deseja continuar? [S/N] ').strip().upper()
    else:
        print('Esta opção não é válida. ')
        resposta = input('Deseja continuar? [S/N] ').strip().upper()