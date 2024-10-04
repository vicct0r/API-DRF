from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    API (HTTP GET) de Cursos 
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data) # recebendo dados
        serializer.is_valid(raise_exception=True) # validando
        serializer.save() # salvando
        return Response(serializer.data, status=status.HTTP_201_CREATED) # retornando para criação da coleção


class AvaliacaoAPIView(APIView):
    """
    API (HTTP GET) de Avaliações
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)