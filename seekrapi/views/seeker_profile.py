from rest_framework import viewsets, filters
from seekrapi.models import SeekerProfile, User, EmployerAction
from rest_framework import serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError

class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SeekerProfile
        fields = ('id', 'user', 'profile_img', 'project_name', 'project_detail', 'project_img', 'project_url', 'bio', 'github_username', 'tech_ed', 'languages')
        depth = 2

class SeekerProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = ('id', 'user', 'profile_img', 'project_name', 'project_detail', 'project_img', 'project_url', 'bio', 'github_username', 'tech_ed', 'languages')


class SeekerProfileViewSet(viewsets.ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer
    filter_fields = ('user','user__id')

    def create (self, request):
        seekr = User.objects.get(pk=request.data['user'])
        profile = SeekerProfile()
        profile.user = seekr
        profile.profile_img = request.data['profile_img']
        profile.project_name = request.data['project_name']
        profile.project_detail = request.data['project_detail']
        profile.project_img = request.data['project_img']
        profile.project_url = request.data['project_url']
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


    def get_queryset(self):
        employer_id = self.request.query_params.get('employer', None)

        if employer_id is not None:
            filterset = SeekerProfile.objects.extra(where=['''
                id IN
                (
                SELECT seekrapi_seekerprofile.id
                FROM  seekrapi_seekerprofile
                LEFT JOIN seekrapi_employeraction
                ON seekrapi_seekerprofile.id = seekrapi_employeraction.seeker_id
                WHERE seekrapi_seekerprofile.id NOT IN 
                (
                    SELECT seeker_id
                    FROM seekrapi_employeraction
                    WHERE employer_id IS %s
                )
                GROUP BY seeker_id
                )
            '''], params=[employer_id])
            return filterset
        else:
            return self.queryset
