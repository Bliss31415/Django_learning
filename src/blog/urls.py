from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('admin/', views.posts, name='admin'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]