from rest_framework import viewsets, filters
from seekrapi.models import CompanyProfile
from rest_framework import serializers

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CompanyProfile
        fields = ('id', 'employer_profile', 'company_name', 'company_logo', 'company_bio')
        
class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    filter_fields = ('employer_profile', 'employer_profile__id')
