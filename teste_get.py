import requests

headers = {'Authorization': 'Token 996cd6f2a75287275c563a6447a69021859d90bc'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 2

# Testando se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Curso de JavaScript'

