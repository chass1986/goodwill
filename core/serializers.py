from rest_framework import serializers
from .models import Territories


class TerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territories
        fields = ('id', 'code', 'name', 'kind')
