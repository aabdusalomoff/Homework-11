from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail_view, name='movie_detail'),
    path('create/', views.movie_create_view, name='movie_create'),
    path('update/<int:pk>/', views.movie_update_view, name='movie_update'),
    path('delete/<int:pk>/', views.movie_delete_view, name='movie_delete')
]

