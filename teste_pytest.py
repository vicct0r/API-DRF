import requests

class TestCurso:
    headers = {'Authorization': 'Token 996cd6f2a75287275c563a6447a69021859d90bc'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}7/', headers=self.headers)
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso em Python",
            "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829044#questions"
        }
        
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso de POO em Python",
            "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829044"
        }
        
        resposta = requests.put(url=f'{self.url_base_cursos}7/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo titulo para o curso POO python",
            "url": "https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/learn/lecture/17829044"
        }
        
        resposta = requests.put(url=f'{self.url_base_cursos}7/', headers=self.headers, data=atualizado)
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}7/', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0