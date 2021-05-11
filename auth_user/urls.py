from django.urls import path
from .views import login_user,signup,home

urlpatterns = [
    path('', home,name='home'),
    path('login', login_user,name='login'),
    path('signup', signup,name='signup'),
]
app_name = 'auth_user'