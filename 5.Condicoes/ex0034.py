# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

retaUm = int(input('Informe o valor da 1ª reta: '))
retaDois = int(input('Informe o valor da 2ª reta: '))
retaTres = int(input('Informe o valor da 3ª reta: '))

if (retaUm + retaDois) > retaTres and (retaDois + retaTres) > retaUm and (retaTres + retaUm) > retaDois:
    print('É possível se formar um triângulo!')
else:
    print('Não é possível se formar um triângulo!')
