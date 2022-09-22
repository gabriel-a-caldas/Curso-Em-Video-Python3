# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tina necessária
# para pintá-la, sabendo que cada litro de tina pinta uma área de 2m^2

largura = int(input('Informa a largura da parede: '))
altura = int(input('Informe a altura da parede: '))

area = largura * altura

tintaNecessaria = area/2

print(f'Para uma parede de {area} m² é preciso {tintaNecessaria} litros de tinta.')