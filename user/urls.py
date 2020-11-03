from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('dashboard/edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.user_logout, name='logout')
]