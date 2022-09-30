# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo
# que ele foi multado.
# A Multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Informe a velocidade que você está: '))

if velocidade > 80:
    print('Você foi multado!')
    print(f'O valor da multa é R${(velocidade-80)*7}.')
else:
    print('Muito bem! Continue andando dentro da lei.')
