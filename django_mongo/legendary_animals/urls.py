from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('add/', views.add_animal),
    path('show/', views.get_all_animals),
    path('legend/', views.get_one_animal)
]