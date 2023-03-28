"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""
from os import system

def notas(*notas,situacao=False):
    """
    Recebe várias notas, mostra a maior, a menor, a média e a situação opcionalmente.

    :param notas: Notas inseridas pelo usuário
    :param situacao: (Opcional) BOA se média maior que 7, RAZOÁVEL se entre
    5 e 7 RUIM se menor que 5.
    :return: Dicionário com os dados.
    """
    totalNotas = {}
    situacaoNotas = ['BOA', 'RAZOÁVEL', 'RUIM']

    totalNotas['total'] = len(notas)
    totalNotas['maior'] = max(notas)
    totalNotas['menor'] = min(notas)
    totalNotas['media'] = round(sum(notas)/totalNotas['total'])
 
    if situacao:
        if totalNotas['media'] < 5:
            totalNotas['situacao'] = situacaoNotas[2]
        elif 5 <= totalNotas['media'] <= 7:
            totalNotas['situacao'] = situacaoNotas[1]
        else:
            totalNotas['situacao'] = situacaoNotas[0]
        return totalNotas
    else:
        return totalNotas

# Programa principal

system('cls')

resposta = notas(10, 5, 6.5, 10, 10, 4, situacao=True)
print(resposta)