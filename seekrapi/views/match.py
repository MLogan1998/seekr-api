from rest_framework import viewsets
from seekrapi.models import Match
from rest_framework import serializers

class MatchSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Match
        fields = ('id', 'employer', 'seeker', 'job')
        
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
