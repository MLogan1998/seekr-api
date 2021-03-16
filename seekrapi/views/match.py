from rest_framework import viewsets
from seekrapi.models import Match, SeekerProfile, JobPosting, EmployerProfile
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError

class MatchSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Match
        fields = ('id', 'employer', 'seeker', 'job', 'seeker_response', 'employer_response')
        
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


    @action(methods=['post'], detail=False)
    def seekermatch(self, request):
        if request.method == 'POST':
            seeker = SeekerProfile.objects.get(pk=request.data['seeker'])
            job = JobPosting.objects.get(pk=request.data['job'])

            obj, created = Match.objects.update_or_create(
                seeker=seeker,
                job=job,
                defaults={'seeker_response': True},
            )

            try:
                obj.save()
                serializer = MatchSerializer(obj, context={'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def employermatch(self, request):
        if request.method == 'POST':
            seeker = SeekerProfile.objects.get(pk=request.data['seeker'])
            job = JobPosting.objects.get(pk=request.data['job'])
            employer = EmployerProfile.objects.get(pk=request.data['employer'])

            obj, created = Match.objects.update_or_create(
                job=job,
                seeker=seeker,
                defaults={'employer_response': True, 'seeker': seeker, 'employer': employer},
            )

            try:
                obj.save()
                serializer = MatchSerializer(obj, context={'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
