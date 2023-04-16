from django.urls import path
from . import views

urlpatterns = [
    # path('poke/', views.Home, name='Home'),
    path('poke/', views.Home.as_view(), name='Home'),
]
