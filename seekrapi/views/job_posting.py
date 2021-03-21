from rest_framework import viewsets, filters
from seekrapi.models import JobPosting, EmployerProfile, CompanyProfile
from rest_framework import serializers
from rest_framework.response import Response
from django.core.exceptions import ValidationError

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = JobPosting
        fields = ('id', 'employer', 'company', 'job_description', 'salary', 'benefits', 'requirements', 'job_title')
        depth = 2

class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = JobPosting
        fields = ('id', 'employer', 'job_description', 'salary', 'benefits', 'requirements', 'job_title')
        
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    filter_fields = ('employer', 'employer__id')


    def create (self, request):
        employer = EmployerProfile.objects.get(pk=request.data['employer'])
        company = CompanyProfile.objects.get(pk=request.data['company'])
        posting = JobPosting()
        posting.employer = employer
        posting.company = company
        posting.job_description = request.data['job_description']
        posting.salary = request.data['salary']
        posting.benefits = request.data['benefits']
        posting.requirements = request.data['requirements']
        posting.job_title = request.data['job_title']

        try:
            posting.save()
            serializer = JobPostingCreateSerializer(posting, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        seeker_id = self.request.query_params.get('seeker', None)

        if seeker_id is not None:
            filterset = JobPosting.objects.extra(where=['''
                id IN
                (
                SELECT seekrapi_jobposting.id
                FROM  seekrapi_jobposting
                LEFT JOIN seekrapi_seekeraction
                ON seekrapi_jobposting.id = seekrapi_seekeraction.job_id
                WHERE seekrapi_jobposting.id NOT IN 
                (
                    SELECT DISTINCT job_id
                    FROM seekrapi_seekeraction
                    WHERE seeker_id IS %s
                )
                )
            '''], params=[seeker_id])
            return filterset
        else:
            return self.queryset
