# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida.

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

notaUm = float(input('Informe qual foi a sua primeira nota: '))
notaDois = float(input('Informe qual foi a sua segunda nota: '))

media = (notaUm + notaDois)/2

if media < 5:
    print(f'Nota: {media}. REPROVADO :(')
elif 5 <= media <= 6.9:
    print(f'Nota: {media}. RECUPERAÇÃO!')
elif media >= 7:
    print(f'Nota: {media}. APROVADO! Parabéns!')
