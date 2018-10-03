from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import DadosPerfil

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'email')


class DadosPerfilSerializer(serializers.ModelSerializer):
    # usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # usuario = serializers.StringRelatedField()
    usuario = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
    class Meta:
        model = DadosPerfil
        # fields = '__all__'
        fields = ('id', 'nome', 'email', 'nome_fantasia', 'website', 'descricao', 'usuario', 'user_id')

