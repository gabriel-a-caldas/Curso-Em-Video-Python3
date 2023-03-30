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


def titulo(mensagem):
    """
    Imprime um título.
    :param mensagem: Mensagem a ser imprimida.
    """
    print('-' * 33)
    print(f'{mensagem}'.center(33))
    print('-' * 33)


def resumo(preco,valorAumentar,valorDiminuir):
    """
    Resumo utilizando todas as funções deste arquivo.
    :param preco: Preço informado pelo usuário
    :param valorAumentar: Valor percentual a ser aumentado do preço.
    :param valorDiminuir: Valor percentual a ser diminuído do preço.
    :return: A definir
    """
    titulo('RESUMO DE VALOR')
    print(f'Preço analisado: \t{floatToCurrency(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{valorAumentar}% de aumento: \t{aumentar(preco,valorAumentar)}')
    print(f'{valorDiminuir}% de redução: \t{diminuir(preco,valorDiminuir)}')
