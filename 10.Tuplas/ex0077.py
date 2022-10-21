"""
Crie um programa que tenha uma tupla com várias palavaras.
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
parametroParadaTupla = int(input('Informe quantas palavras deseja inserir: '))

tuplaPalavrasAleatorias = tuple(str(input('Insira uma palavra: '))for c in range(0,parametroParadaTupla))

tuplaVogais = ('a','e','i','o','u')

