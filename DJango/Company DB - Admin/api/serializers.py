from rest_framework import serializers
from .models import Company, Employee

# Converts model data to JSON format

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField() # Disables update for id field 
    
    class Meta:
        model = Company
        fields = '__all__' # Also possible to use custom selection of fields from the model


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['name', 'email', 'phone', 'position', 'company']


