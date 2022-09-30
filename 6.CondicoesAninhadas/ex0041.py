# Refaça o desafio dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais 
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes.

retaUm = int(input('Informe o 1º lado do triângulo: '))
retaDois = int(input('Informe o 2º lado do triângulo: '))
retaTres = int(input('Informe o 3º lado do triângulo: '))

if (retaUm + retaDois) > retaTres and (retaDois + retaTres) > retaUm and (retaTres + retaUm) > retaDois:
    print('É possível se formar um triângulo! E é um:')
    if retaUm == retaDois == retaTres:
        print('Triângulo equilátero!')
    elif retaUm == retaDois or retaUm == retaTres or retaDois == retaTres:
        print('Triãngulo isóceles!')
    else:
        print('Triângulo escaleno!')
else:
    print('Não é possível se formar um triângulo!')