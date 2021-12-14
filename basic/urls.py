from django.urls import path, include
from .views import index, content, team 


urlpatterns = [

    path('', index, name='dashboard'),
    path('content/', content, name='content'),
    path('team/', team, name='team'),
]