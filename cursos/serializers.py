from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True} # impedindo acesso aos emails do modelo, para preservar dados dos usuários
        }
        model = Avaliacao
        
        fields = [              # fields = [] deverá ter tudo que eu quiser apresentar no JSON,
            'id',               # ou seja, tudo que eu quiser apresentar para o meu Cliente.
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        ]


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        ]