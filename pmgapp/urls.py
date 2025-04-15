from django.urls import path
from . import views

app_name = 'packet'

urlpatterns = [
    path('', views.packet_list, name='packet_list'),
    path('<int:packet_number>/', views.packet_detail, name='packet_detail'),
    path('<int:packet_number>/vymohy/', views.packet_vymohy, name='packet_vymohy'),
]
