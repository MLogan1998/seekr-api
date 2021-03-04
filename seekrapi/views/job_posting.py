from rest_framework import viewsets
from seekrapi.models import JobPosting
from rest_framework import serializers

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = JobPosting
        fields = ('id', 'employer', 'job_description', 'salary', 'benefits')
        
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
