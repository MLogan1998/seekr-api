from rest_framework import viewsets, filters
from seekrapi.models import EmployerProfile
from rest_framework import serializers

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EmployerProfile
        fields = ('id', 'user', 'profile_img')
        
class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    filter_fields = ('user','user__id')
