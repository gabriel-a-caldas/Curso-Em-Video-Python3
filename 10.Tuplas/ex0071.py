"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
porExtenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove',
'Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',
'Dezenove','Vinte')

escolha = int(input('Qual número você deseja ver por extenso? '))
while escolha < 0 or escolha > 20:
    print('Tente novamente.')
    escolha = int(input('Qual número você deseja ver por extenso? '))
print(f'Você digitou o número {porExtenso[escolha]}')
