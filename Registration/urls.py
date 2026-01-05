from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.select_event_type, name='select_event_type'),
    path('events/<str:event_type>/', views.event_list, name='event_list'),
    path('register/<int:event_id>/', views.event_register, name='event_register'),
]
