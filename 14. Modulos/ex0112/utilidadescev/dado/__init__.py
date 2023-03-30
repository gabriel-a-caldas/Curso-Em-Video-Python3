"""
Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado. Crie uma
função chamada leiaDinheiro() que seja capaz de funcionar com a função input(), mas com uma validação
de dados para aceitar apenas valores que sejam monetários.
"""
def leiaDinheiro(preco):
    
    valido = False
    while not valido:
        entrada = str(input(preco)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'\033[0;31mERRO: \"{entrada}\" não é um preço válido!\033[m')
        else:
            valido = True
            return float(entrada)
