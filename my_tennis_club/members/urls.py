from django.urls import path
from . import views

urlpatterns = [
    # for python 3.8
    # path('members/', views.members, name='members'),

    # doe python 3.10
    path('members/', views.members, name='members'),
]

