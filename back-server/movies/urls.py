from django.urls import path
from . import views, views_tmdb

app_name='movies'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('popular/', views.get_popular, name='popular'),
    path('tmdb/', views_tmdb.tmdb_data),
    # path('get_youtube/', views.get_youtube),
    path('api/v1/', views.movie_list),
    path('<int:movie_pk>/like', views.like, name='like'),
]
