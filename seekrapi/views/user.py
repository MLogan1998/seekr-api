from rest_framework import viewsets
from rest_framework import serializers
from seekrapi.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'is_seeker', 'has_company', 'has_profile', 'has_listing', 'first_name', 'last_name')
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
