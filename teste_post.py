import requests

headers = {'Authorization': 'Token 996cd6f2a75287275c563a6447a69021859d90bc'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Curso de Banco de Dados",
    "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829036#questions"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HTTP
assert resultado.status_code == 201