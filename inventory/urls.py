from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Item_id>/', views.view, name='view'),
    path('add/', views.add, name='add'),
    path('edit/<int:Item_id>/', views.edit, name='edit'),
    path('use/<int:Item_id>/', views.use, name='use'),
    path('delete/<int:Item_id>/', views.delete, name='delete'),
    path('delete/<int:Item_id>/true', views.deleteTrue, name='deleteTrue')
]

