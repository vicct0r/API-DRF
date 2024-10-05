from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
API V1.0
"""

# Lista a coleção CURSOS e cria um objeto CURSO
class CursosAPIView(generics.ListCreateAPIView):
    """
    ListCreateAPIView permite a listagem da coleção de objetos 'Curso' e também me permite criar um novo objeto desta coleção
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Manipula somente um objeto 'curso' dentro da coleção
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView busca um objeto 'Curso' específico para ser manipulado com todas as opções de CRUD possíveis 
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    
    # get_queryset agora poderá receber um 'curso_pk' como argumento para tentar trazer todas as avaliacoes
    # especificas do objeto 'Curso' que estamos passando o parâmetro pk em kwargs na URL 'api/v1/cursos/<int:curso_pk>/avaliacoes'
    
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    # get_object agora faz com que seja possível passar o 'curso_pk' como parâmetro para ver uma avaliacao
    # específica na rota em que poderemos ver todas as avaliacoes de um objeto 'Curso' especifico, ou seja,
    # por estarmos fazendo isso, precisamos passar 'pk' para a URL 'api/v1/avaliacoes/<int:pk>/' e também
    # precisaremos de 'curso_pk' para referenciar a URL 'api/v1/cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>'
    
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2.0
"""

class CursoViewSet(viewsets.ModelViewSet):
    # ModelViewSet me dá todas as operações de CRUD do meu Model 'Curso'
    # e o decorador '@action' já faz com que o router que instânciei no meu módulo cursos.urls
    # crie automaticamente o endpoint (rota) para esta página da View

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True) # curso.avaliacoes.all() 'avaliacoes' é o related_name da chave estrangeira 'curso' dentro de Avaliacoes no Model
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer