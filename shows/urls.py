from django.urls import path
from .views import create_show, show_show

urlpatterns = [
    path('',show_show,name='show'),
    path('add',create_show,name='create'),
]

app_name = 'shows'