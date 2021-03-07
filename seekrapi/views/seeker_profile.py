from rest_framework import viewsets
from seekrapi.models import SeekerProfile
from rest_framework import serializers

class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SeekerProfile
        fields = ('id', 'user', 'profile_img', 'project_name', 'project_detail', 'project_img', 'github_username', 'tech_ed', 'languages')
        depth = 2
        
class SeekerProfileViewSet(viewsets.ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer
