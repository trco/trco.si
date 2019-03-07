from django.urls import path

from . import views


app_name = 'dfs'
urlpatterns = [
    path('create/', views.CreateMovieView.as_view(), name='create_movie'),
    path('update/', views.UpdateMovieView.as_view(), name='update_movie'),
]
