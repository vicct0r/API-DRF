import requests 

# GET Avaliacoes
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# MANIPULANDO A VARIÁVEL (avaliacoes) QUE ACABAMOS DE CRIAR:

# Acessando o codigo de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta 
# print(avaliacoes.json()) # traz um dicionário dos dados 

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a proxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os dados da página
# print(avaliacoes.json()['results'])


# GET Avaliacao
avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/6/')
# print(avaliacao)