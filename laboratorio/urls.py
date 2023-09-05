from django.urls import path
from .views import list_laboratorio, new_laboratorio, update_laboratorio, delete_laboratorio

urlpatterns = [
    path('', list_laboratorio, name="list_laboratorio"),
    path('add', new_laboratorio, name="new_laboratorio"),
    path('update/<int:id>/', update_laboratorio, name="update_laboratorio"),
    path('delete/<int:id>/', delete_laboratorio, name="delete_laboratorio"),
    
]