from rest_framework import viewsets
from seekrapi.models import SeekerProfile, User
from rest_framework import serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError

class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SeekerProfile
        fields = ('id', 'user', 'profile_img', 'project_name', 'project_detail', 'project_img', 'bio', 'github_username', 'tech_ed', 'languages')
        depth = 2

class SeekerProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = ('id', 'user', 'profile_img', 'project_name', 'project_detail', 'project_img', 'bio', 'github_username', 'tech_ed', 'languages')


class SeekerProfileViewSet(viewsets.ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer

    def create (self, request):
        seekr = User.objects.get(pk=request.data['user'])
        profile = SeekerProfile()
        profile.user = seekr
        profile.profile_img = request.data['profile_img']
        profile.project_name = request.data['project_name']
        profile.project_detail = request.data['project_detail']
        profile.project_img = request.data['project_img']
        profile.bio = request.data['bio']
        profile.github_username = request.data['github_username']
        profile.tech_ed = request.data['tech_ed']

        try:
            profile.save()
            profile.languages.set(request.data["languages"])
            profile.save()
            serializer = SeekerProfileCreateSerializer(profile, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
