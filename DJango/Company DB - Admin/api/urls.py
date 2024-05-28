from django.contrib import admin
from django.urls import path, include

from .views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers  # Organizes API's for URL endpoints 

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls))
]