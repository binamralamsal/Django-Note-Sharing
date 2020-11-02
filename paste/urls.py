from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('text/<int:pk>', views.get_text, name='get_text'),
    path('dashboard/add/', views.add_text_form, name='add_text_form'),
    path('dashboard/add_text/', views.add_text, name='add_text'),
    path('dashboard/edit/<int:id>/', views.edit_text_form, name='edit_text_form'),
    path('dashboard/edit_text/<int:id>/', views.edit_text, name="edit_text"),
    path('dashboard/delete_text/', views.delete_text, name='delete_text'),
    path('dashboard/', views.my_pastes, name='dashboard')
]