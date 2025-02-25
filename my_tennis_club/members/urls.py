from django.urls import path
from . import views

urlpatterns =[
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details  , name='members'),
    path('members/new_member', views.new_member, name='new_member'),
    path('members/new_member/save', views.create_member, name='create_member'),
    path('members/delete/<int:id>', views.delete  , name='delete_member'),
    path('members/update/<int:id>', views.update  , name='delete_member'),
    path('members/update/<int:id>/save', views.update_member  , name='update_member'),
]
