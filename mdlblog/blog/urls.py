from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('posts/<int:post_id>/', views.Post.as_view(), name='post'),
]