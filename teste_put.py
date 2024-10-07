import requests

headers = {'Authorization': 'Token 996cd6f2a75287275c563a6447a69021859d90bc'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_valor = {
    "titulo": "alguma coisa",
    "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829040#questions"
}

resposta = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=novo_valor)

assert resposta.status_code == 200
assert resposta.json()['titulo'] == novo_valor['titulo'] # conferindo se os titulos estão iguais

