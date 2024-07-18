from django.urls import path
from huespedes import views


urlpatterns=[
    path('huespedes/',views.Huespedes.as_view(), name='huespedes'),
    path('huespedes/crear/',views.CrearHuesped.as_view(), name='crear_huesped'),
    path('huespedes/<int:pk>/',views.VerHuesped.as_view(), name='ver_huesped'),
    path('huespedes/<int:pk>/actualizar/',views.ActualizarHuesped.as_view(), name='actualizar_huesped'),
    path('huespedes/<int:pk>/eliminar/',views.EliminarHuesped.as_view(), name='eliminar_huesped'),
    
]