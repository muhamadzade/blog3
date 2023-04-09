
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post100/', views.post100, name='post100'),
    path('post/<int:pk>/', views.post_detail, name='post_detail1'),
]
