from django.urls import path
from .views import create_show, show_show, allitems

urlpatterns = [
    path('',show_show,name='show'),
    path('add',create_show,name='create'),
    path('allitems/<str:catagory_name>',allitems,name='allitems'),
]

app_name = 'shows'