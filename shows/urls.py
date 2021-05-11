from django.urls import path
from .views import create_show, show_show, allitems,show_item

urlpatterns = [
    path('',show_show,name='show'),
    path('add',create_show,name='create'),
    path('allitems/<str:catagory_name>',allitems,name='allitems'),
    path('showitem/<int:pk>',show_item,name='show_item'),
]

app_name = 'shows'