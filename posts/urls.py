from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('read/<int:pk>', views.read, name='read'),
    path('listall', views.listall, name='listall'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('contact', views.contact, name='contact')
]