from django.urls import path
from live import views




urlpatterns=[
    path('', views.home4, name='home'),
    path('random', views.home3, name='home2'),
]