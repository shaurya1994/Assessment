from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()  # Creating the form from Django REST framework
    serializer_class = CompanySerializer

    # Custom query to employees for one particular company
    
    # companies/{companyID}/employees 
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        
        # try except block if invalid company entered in api url
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company) 

            # To convert into JSON format
            emp_serializer = EmployeeSerializer(
                employees, 
                many=True,
                context={'request':request}
            )
            return Response(emp_serializer.data) 
        
        except Exception as e:
            print(e)
            return Response({'message': 'Records do not exist'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
