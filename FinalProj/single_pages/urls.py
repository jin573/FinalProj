from django.urls import path
from . import views

urlpatterns = [
    path('company_shoesmall/', views.company_shoesmall),
    path('my_page/', views.my_page),
    path('', views.homepage),
]