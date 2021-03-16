from rest_framework import viewsets
from seekrapi.models import EmployerAction
from rest_framework import serializers

class EmployerActionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EmployerAction
        fields = ('id', 'employer', 'employer_response', 'seeker', 'job')
        
class EmployerActionViewSet(viewsets.ModelViewSet):
    queryset = EmployerAction.objects.all()
    serializer_class = EmployerActionSerializer
