from rest_framework import viewsets
from seekrapi.models import Languages
from rest_framework import serializers

class LanguagesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Languages
        fields = ('id', 'name')
        
class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
