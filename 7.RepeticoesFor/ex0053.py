# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas poessoas ainda não atingiram a maioridade
# e quantas já são maiores.
import datetime

dataAtual = datetime.date.today()
anoAtual = dataAtual.year

contadorMaioridade = 0
contadorMenoridade = 0

for i in range(0, 7):
    anoNascimento = int(input('Informe o seu ano de nascimento: '))
    if anoAtual - anoNascimento < 18:
        contadorMaioridade += 1 
    else:
        contadorMenoridade += 1
print(f'Há: {contadorMaioridade} pessoas maiores.')
print(f'Há: {contadorMenoridade} pessoas menores.')