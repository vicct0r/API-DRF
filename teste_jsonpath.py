import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]') # pegando o primeiro elemento de 'avaliacoes'
# print(primeiro)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome') # pegando o 'nome' do primeiro elemento
# print(nome)

# Todos os nomes das pessoas que avaliaram o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)

# Todas as notas dadas pelos avaliadores
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)