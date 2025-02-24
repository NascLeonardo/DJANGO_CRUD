from django.urls import path
from . import views

urlpatterns =[
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details  , name='members'),
    path('members/new_member', views.new_member, name='new_member'),
]
