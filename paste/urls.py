from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('text/<int:pk>', views.get_text, name='get_text'),
    path('add/', views.add_text_form, name='add_text_form'),
    path('add_text/', views.add_text, name='add_text')
]