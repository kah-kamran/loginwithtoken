from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views

urlpatterns = [
    path('hello/', views.login),
    path('api/sampleapi', views.sample_api),
]