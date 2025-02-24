from django.urls import path
from . import views

urlpatterns =[
    path('equipments/', views.main_equipments, name='equipments'),
    path('equipments/all', views.equipments, name='equipments'),
    path('equipments/details/<int:id>', views.details  , name='equipments'),
]
