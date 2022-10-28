"""
Crie uma tupla preenchida com os 20 primerios colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""

primeiroDaLista = segundoDaLista = ''

classificacao = ('Palmeiras', 'Flamengo','Internacional','Grêmio',
                'São Paulo','Atlético','Athletico-PR','Cruzeiro','Botafogo','Santos',
                'Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport',
                'América-MG','Vitória','Paraná')
tamanho = len(classificacao)
print('==== PRIMEIROS COLOCADOS ====') # PRIMEIROS COLOCADOS
for posicao in range(0,5):
    print(f'{posicao+1}º Lugar: {classificacao[posicao]}')
print('---'*6)
print('==== ÚLTIMOS COLOCADOS ====') # ÚLTIMOS COLOCADOS
for posicao in range(tamanho-1,tamanho-5,-1):
    print(f'{posicao+1}º Lugar: {classificacao[posicao]}')
print('---'*6)

print(f'Em ordem alfabética: {sorted(classificacao)}') # Ordem alfabética

posicaoChapecoense = classificacao.index('Chapecoense')
print(f'\nA Chapecoense está na {posicaoChapecoense+1}ª posição.') # POSIÇÃO DA CHAPECOENSE