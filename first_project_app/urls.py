from django.urls import path
from first_project_app import views




urlpatterns=[
    path('', views.home, name='home'),
    path('random', views.home2, name='home2'),
    path('calc/', views.calc, name='calc'),
    path('calc/<int:number>', views.calc_int, name='calc_int'),
    path('dict/<str:text>', views.get_data, name='get_data')
]