"""

Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade().

Faça também um programa que importe esse módulo e use algumas dessa funções.

"""
def aumentar(preco=0,valor=0):
    """
    Recebe um valor e o aumenta percentualmente
    :param preco: Preço do produto
    :param valor: Percentual a ser aumentado.
    :return: Retorna o valor já adicionado ao percentual.
    """
    percentualTotal =  preco * (valor/100)
    return preco  + percentualTotal


def diminuir(preco=0,valor=0):
    """
    Recebe um valor e o diminui percentualmente
    :param preco: Preço do produto
    :param valor: Percentual a ser aumentado.
    :return: Retorna o valor já subtraído ao percentual.
    """
    percentualTotal =  preco * (valor/100)
    return preco  - percentualTotal


def metade(preco=0):
    """
    Recebe um valor e retorna a metade dele.
    :param preco: Preço do produto.
    :return: Retorna a metade do valor.
    """
    return preco/2


def dobro(preco=0):
    """
    Recebe um valor e retorna o dobro dele.
    :param preco: Preço do produto.
    :return: Retorna o dobro do valor.
    """
    return preco * 2


def floatToCurrency(preco=0,moeda='R$'):
    """
    Recebe um valor numérico e transforma em monetário.
    :param preco: Valor inteiro
    :valor monetário:
    """
    return f'{moeda}{preco:.2f}'.replace('.',',')
