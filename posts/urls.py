from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('posts', views.posts, name='posts'),
    path('create_get', views.create_get, name='create_get'),
    path('create_post', views.create_post, name='create_post'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('contact', views.contact, name='contact')
]