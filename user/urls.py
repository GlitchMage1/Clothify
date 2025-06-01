from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('signup/', signup_view, name='signup'),
]