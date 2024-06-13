from django.urls import path
from inicio import views

urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('huespedes/', views.huespedes,name='huespedes'),
    path('huesped/registro/',views.crear_huesped,name='crear_huesped'),
    
]



