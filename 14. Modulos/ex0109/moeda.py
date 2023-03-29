"""

Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade().

Faça também um programa que importe esse módulo e use algumas dessa funções.

"""
def aumentar(preco=0,valor=0,formatado=True):
    """
    Recebe um valor e o aumenta percentualmente
    :param preco: Preço do produto
    :param valor: Percentual a ser aumentado.
    :param formatado: Formata ou não o valor do preço
    :return: Retorna o valor já adicionado ao percentual.
    """
    percentualTotal =  preco * (valor/100)
    
    if formatado:
        return floatToCurrency(percentualTotal)
    else:
        return preco  + percentualTotal


def diminuir(preco=0,valor=0,formatado=True):
    """
    Recebe um valor e o diminui percentualmente
    :param preco: Preço do produto
    :param valor: Percentual a ser aumentado.
    :param formatado: Formata ou não o valor do preço
    :return: Retorna o valor já subtraído ao percentual.
    """
    percentualTotal =  preco * (valor/100)
    
    if formatado:
        return floatToCurrency(percentualTotal)
    else:
        return preco  + percentualTotal


def metade(preco=0,formatado=True):
    """
    Recebe um valor e retorna a metade dele.
    :param preco: Preço do produto.
    :param formatado: Formata ou não o valor do preço
    :return: Retorna a metade do valor.
    """
    if formatado:
        return floatToCurrency(preco/2)
    else:
        return preco/2


def dobro(preco=0,formatado=True):
    """
    Recebe um valor e retorna o dobro dele.
    :param preco: Preço do produto.
    :param formatado: Formata ou não o valor do preço
    :return: Retorna o dobro do valor.
    """
    if formatado:
        return floatToCurrency(preco/2)
    else:
        return preco * 2


def floatToCurrency(preco=0,moeda='R$'):
    """
    Recebe um valor numérico e transforma em monetário.
    :param preco: Valor inteiro
    :param formatado: Formata ou não o valor do preço
    :valor monetário:
    """
    return f'{moeda}{preco:.2f}'.replace('.',',')
