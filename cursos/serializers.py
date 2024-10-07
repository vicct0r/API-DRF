from rest_framework import serializers
from django.db.models import Avg # Função de Agregação (Average/Média)
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

    def validate_avaliacao(self, valor):
        if valor in range(1, 10):
            return valor
        raise serializers.ValidationError('A avaliação deve ser de 1 à 9')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True) # Trazendo todas avaliações do Curso
    
    # Primary Key Related Field
    #avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # Hyperlinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        ]

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2