from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('employee/create/', views.create, name='create'),
    path('employee/edit/<uuid:pk>', views.edit, name='edit'),
    path('employee/delete/<uuid:pk>', views.delete, name='delete'),
]