# core/serializers.py
from rest_framework import serializers
from .models import Area, Platillo, Pedido, Parte


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class PlatilloSerializer(serializers.ModelSerializer):
    areas = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all(), many=True)

    class Meta:
        model = Platillo
        fields = '__all__'


class ParteSerializer(serializers.ModelSerializer):
    platillo = PlatilloSerializer()
    area = AreaSerializer()

    class Meta:
        model = Parte
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    partes = ParteSerializer(many=True, read_only=True)
    mesero = serializers.StringRelatedField()

    class Meta:
        model = Pedido
        fields = '__all__'
