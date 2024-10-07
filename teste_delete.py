import requests

headers = {'Authorization': 'Token 996cd6f2a75287275c563a6447a69021859d90bc'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resposta = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

assert resposta.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resposta.text) == 0