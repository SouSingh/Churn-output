from django.contrib import admin
from django.urls import path
from .views import Home, Api, ApiVeiw

urlpatterns = [
    path('', Home , name='home'),
    path('Api', Api, name='api'),
    path('Api/query/q=<str:param>/', ApiVeiw )
]
