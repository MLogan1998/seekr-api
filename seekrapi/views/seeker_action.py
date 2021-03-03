from rest_framework import viewsets
from seekrapi.models import SeekerAction
from rest_framework import serializers

class SeekerActionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SeekerAction
        fields = ('id', 'seeker', 'seeker_response', 'job')
        
class SeekerActionViewSet(viewsets.ModelViewSet):
    queryset = SeekerAction.objects.all()
    serializer_class = SeekerActionSerializer
