from django.urls import path
from .views import login_user,signup,home,logout_user

urlpatterns = [
    path('', home,name='home'),
    path('login', login_user,name='login'),
    path('signup', signup,name='signup'),
    path('logout', logout_user,name='logout'),
]
app_name = 'auth_user'